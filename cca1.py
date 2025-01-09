import streamlit as st
from openai import OpenAI

# Inject Bootstrap CSS
st.markdown(
    """
        <!-- Favicon -->
        <link rel="icon" href="https://www.cancepro.com/img/favicon.png">

        <!-- Google Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Poppins:200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i&display=swap" rel="stylesheet">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://www.cancepro.com/css/bootstrap.min.css">
        <!-- Nice Select CSS -->
        <link rel="stylesheet" href="https://www.cancepro.com/css/nice-select.css">
        <!-- Font Awesome CSS -->
        <link rel="stylesheet" href="https://www.cancepro.com/css/font-awesome.min.css">
        <!-- icofont CSS -->
        <link rel="stylesheet" href="https://www.cancepro.com/css/icofont.css">
        <!-- Slicknav -->
        <link rel="stylesheet" href="https://www.cancepro.com/css/slicknav.min.css">
        <!-- Owl Carousel CSS -->
        <link rel="stylesheet" href="https://www.cancepro.com/css/owl-carousel.css">
        <!-- Datepicker CSS -->
        <link rel="stylesheet" href="https://www.cancepro.com/css/datepicker.css">
        <!-- Animate CSS -->
        <link rel="stylesheet" href="https://www.cancepro.com/css/animate.min.css">
        <!-- Magnific Popup CSS -->
        <link rel="stylesheet" href="https://www.cancepro.com/css/magnific-popup.css">

        <!-- Medipro CSS -->
        <link rel="stylesheet" href="https://www.cancepro.com/css/normalize.css">
        <link rel="stylesheet" href="https://www.cancepro.com/style.css">
        <link rel="stylesheet" href="https://www.cancepro.com/css/responsive.css">
    """,
    unsafe_allow_html=True
)


# Create a Bootstrap navbar
# st.markdown(
#     """
#     <nav class="navbar navbar-expand-lg navbar-light bg-light">
#         <a class="navbar-brand" href="#">My App</a>
#         <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#             <span class="navbar-toggler-icon"></span>
#         </button>
#         <div class="collapse navbar-collapse" id="navbarNav">
#             <ul class="navbar-nav">
#                 <li class="nav-item active">
#                     <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
#                 </li>
#                 <li class="nav-item">
#                     <a class="nav-link" href="#">Features</a>
#                 </li>
#                 <li class="nav-item">
#                     <a class="nav-link" href="#">Pricing</a>
#                 </li>
#                 <li class="nav-item">
#                     <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
#                 </li>
#             </ul>
#         </div>
#     </nav>
#     """,
#     unsafe_allow_html=True
# )





st.markdown(
    """
        
		<!-- Header Area -->
		<header class="header" id="header">
			<!-- Header Inner -->
			<div class="header-inner" style="border-bottom:1px solid red; margin-bottom:10px;">
				<div class="container">
					<div class="inner">
						<div class="row">
							<div class="col-lg-3 col-md-3 col-12">
								<!-- Start Logo -->
								<div class="logo">
									<a href="index.html"><img src="https://www.cancepro.com/img/icon/CancePro_Icon.png" alt="#"></a>
								</div>
								<!-- End Logo -->
								<!-- Mobile Nav -->
								<div class="mobile-nav"></div>
								<!-- End Mobile Nav -->
							</div>
							<div class="col-lg-9 col-md-9 col-12">
								<!-- Main Menu -->
								<div class="main-menu">
									<nav class="navigation">
										<ul class="nav menu" style="float: right;">
											<li><a href="https://www.cancepro.com">Go Home</a></li>
											<li><a href="https://canceproit.pythonanywhere.com/getxray">X-Ray Analysis</a></li>
											<li><a href="https://canceproit.pythonanywhere.com/getliveanalysis">Cancer Records</a></li>
										</ul>
									</nav>
								</div>
								<!--/ End Main Menu -->
							</div>
						</div>
					</div>
				</div>
			</div>
			<!--/ End Header Inner -->
		</header>
		<!-- End Header Area -->


    """,
    unsafe_allow_html=True
)

# Show title and description.
st.write(
    "Our information relies on well known Cancer research institutes research documents that are publicly available. Ask a cancer related question in the below box, get relevant information."
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# openai_api_key = st.text_input("OpenAI API Key", type="password")
# openai_api_key = 'skproj-VLAnUqPbIQTfG1vvnxMAKwY46H7_svlnFOPNWnsl1ch7K8x68MLX3JWkOE4XDVy--Ou9kFoW99T3BlbkFJG0cBpvXKtW_sTI7T0LJ2dyJnR1zYggrbVhfWatqvDPTzollNzdmhzPhh8tOZMhWNT0tk-ykMMA'
openai_api_key = 'a'

if not openai_api_key:
    st.info("We are under maintenance, please check back.")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("Ask Me Here..."):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

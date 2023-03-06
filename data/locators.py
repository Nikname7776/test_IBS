from dataclasses import dataclass


@dataclass
class URLSwagger:
    swagger_url: str = 'https://reqres.in/api-docs/'


@dataclass
class MainPage:
    endpoint: str = 'endpoint'
    main_header: str = 'main-header'
    window_endpoint_class: str = 'console try-api-links'
    response_code: str = 'response-code'
    output_response: str = 'output-response'
    fake_data_text: str = 'Fake data'
    real_responses_text: str = 'Real responses'
    always_on_text: str = 'Always-on'
    swagger_test: str = 'Swagger logo'
    send_keys_field: str = 'oneTimeAmount'
    text: str = '25'
    breathe: str = 'Support ReqRes'
    scroll_down: str = "window.scrollTo(0, document.body.scrollHeight);"
    scroll_from_element: str = "arguments[0].scrollIntoView();"
    many_text: str = 'Оплатить картой'
    swagger_button: str = "[alt='Swagger logo']"
    status_code_200: str = '200'
    some_text: str = 'Give it a try'

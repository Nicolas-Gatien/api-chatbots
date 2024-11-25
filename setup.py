from setuptools import find_packages, setup

setup(
    name='api_chatbots',
    packages=find_packages(include=['api_chatbots']),
    version='0.1.0',
    description='Facilitates interaction with API llms such as ChatGPT, Claude, and Gemini...',
    author='Nicolas Gatien',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
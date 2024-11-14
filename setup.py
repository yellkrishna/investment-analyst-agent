from setuptools import setup, find_packages

setup(
    name="junior_investment_analyst_agent",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here, for example:
        # "requests>=2.24.0",
    ],
    test_suite="tests",  # This specifies the test directory
    tests_require=[
        "pytest",  # You can add other test dependencies here
    ],
)

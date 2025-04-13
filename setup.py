import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding='utf-8')

requirements = [
    'requests<3.0,>=2.25.1',
    'PySocks==1.7.1',
    'SpeechRecognition==3.8.1',
    'pydub==0.25.1',
    'selenium',
]

setup(
    name='anti-recaptcha',
    version='0.0.2',
    author='Dragon',
    license='MIT',
    url='https://github.com/dragon0041/anti-recaptcha',
    install_requires=requirements,
    keywords=[
        'recaptcha solver', 'recaptcha', 'bypass recaptcha', 'anti recaptcha', 'google recaptcha',
        'captcha solver', 'captcha bypass', 'solve captcha', 'auto captcha solve',
        'recaptcha v2', 'recaptcha v3', 'v2 captcha solver', 'v3 captcha solver',
        'google captcha', 'captcha breaker', 'recaptcha breaker',
        'python recaptcha solver', 'recaptcha solver python',
        'ai captcha solver', 'machine learning captcha solver', 'deep learning captcha',
        'captcha automation', 'captcha bot', 'recaptcha bot',
        'selenium recaptcha', 'selenium captcha solver', 'selenium recaptcha solver',
        'undetected chromedriver', 'headless browser recaptcha', 'headless selenium captcha',
        'python bot captcha', 'bypass google recaptcha', 'captcha cracking tool',
        'solve recaptcha automatically', 'recaptcha bypass script',
    ],
    description='Python reCaptcha V2 & V3 solver.',
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
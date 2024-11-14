# tests/test_coordination_agent.py

from agents.coordination_agent import coordination_agent

def test_coordination_agent():
    ticker = 'AAPL'
    report = coordination_agent(ticker)
    assert report['ticker'] == ticker
    assert report['status'] == 'success'
    assert 'fundamental_analysis' in report
    assert 'technical_analysis' in report
    print("Coordination agent test passed!")

if __name__ == '__main__':
    test_coordination_agent()

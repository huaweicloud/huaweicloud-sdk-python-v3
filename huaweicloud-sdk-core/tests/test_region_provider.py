import stat
import sys

from huaweicloudsdkcore.region.cache import EnvRegionCache, ProfileRegionCache
from huaweicloudsdkcore.region.provider import EnvRegionProvider, ProfileRegionProvider, RegionProviderChain
from huaweicloudsdkcore.region.region import Region

import pytest
import os

SERVICE_NAME = "Service"
REGION_ID = "region-id-1"
ENDPOINT = "https://{}.{}.myhuaweicloud.com".format(SERVICE_NAME.lower(), REGION_ID)
REGION_STR = """SERVICE:
  - id: region-id-1
    endpoint: 'https://service.region-id-1.myhuaweicloud.com'
"""


def test_env_region_provider():
    # test singleton
    assert EnvRegionCache() is EnvRegionCache()
    # test not found
    provider = EnvRegionProvider(SERVICE_NAME)
    assert provider.get_region(REGION_ID) is None
    # test found
    env_name = "HUAWEICLOUD_SDK_REGION_{}_{}".format(SERVICE_NAME.upper(), REGION_ID.replace("-", "_").upper())
    os.environ[env_name] = ENDPOINT
    actual_region = provider.get_region(REGION_ID)
    assert actual_region
    expected_region = Region(REGION_ID, ENDPOINT)
    assert expected_region.id == actual_region.id
    assert expected_region.endpoint == actual_region.endpoint


def test_profile_region_provider():
    platform = sys.platform
    if platform.startswith("win32"):
        home_path = os.environ.get("USERPROFILE")
    elif platform.startswith("linux") or sys.platform.startswith("darwin"):
        home_path = os.environ.get("HOME")
    else:
        assert False
    filename = "test_regions.yaml"
    path = os.path.join(home_path, filename)
    os.environ["HUAWEICLOUD_SDK_REGIONS_FILE"] = path

    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    modes = stat.S_IWUSR | stat.S_IRUSR
    with os.fdopen(os.open(path, flags, modes), 'w') as f:
        f.write(REGION_STR)

    # test singleton
    assert ProfileRegionCache() is ProfileRegionCache()
    provider = ProfileRegionProvider(SERVICE_NAME)
    try:
        # test found
        actual_region = provider.get_region(REGION_ID)
        assert actual_region
        expected_region = Region(REGION_ID, ENDPOINT)
        assert expected_region.id == actual_region.id
        assert expected_region.endpoint == actual_region.endpoint
    except AssertionError:
        assert False
    finally:
        if os.path.isfile(path):
            os.remove(path)
    # test not found
    region = provider.get_region("not-exist-1")
    assert region is None


def test_region_provider_chain():
    chain = RegionProviderChain.get_default_region_provider_chain(SERVICE_NAME)
    # test not found
    assert chain.get_region("not-exist-2") is None
    # test found
    region_id = "test-region-2"
    endpoint = "https://test.service.com"
    env_name = "HUAWEICLOUD_SDK_REGION_{}_{}".format(SERVICE_NAME.upper(), region_id.replace("-", "_").upper())
    os.environ[env_name] = endpoint
    actual_region = chain.get_region(region_id)
    assert actual_region
    expected_region = Region(region_id, endpoint)
    assert expected_region.id == actual_region.id
    assert expected_region.endpoint == actual_region.endpoint


if __name__ == '__main__':
    pytest.main()

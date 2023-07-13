# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config': 'dict(str, str)',
        'regions': 'list[dict(str, str)]'
    }

    attribute_map = {
        'config': 'config',
        'regions': 'regions'
    }

    def __init__(self, config=None, regions=None):
        """ShowConfigResponse

        The model defined in huaweicloud sdk

        :param config: mainRegion,obs_domain,disktype,process_and_it及以后增加的信息
        :type config: dict(str, str)
        :param regions: region数组
        :type regions: list[dict(str, str)]
        """
        
        super(ShowConfigResponse, self).__init__()

        self._config = None
        self._regions = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if regions is not None:
            self.regions = regions

    @property
    def config(self):
        """Gets the config of this ShowConfigResponse.

        mainRegion,obs_domain,disktype,process_and_it及以后增加的信息

        :return: The config of this ShowConfigResponse.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ShowConfigResponse.

        mainRegion,obs_domain,disktype,process_and_it及以后增加的信息

        :param config: The config of this ShowConfigResponse.
        :type config: dict(str, str)
        """
        self._config = config

    @property
    def regions(self):
        """Gets the regions of this ShowConfigResponse.

        region数组

        :return: The regions of this ShowConfigResponse.
        :rtype: list[dict(str, str)]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ShowConfigResponse.

        region数组

        :param regions: The regions of this ShowConfigResponse.
        :type regions: list[dict(str, str)]
        """
        self._regions = regions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

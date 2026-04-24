# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScreenRecordsConfigResultReqConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'traffic_limit': 'int'
    }

    attribute_map = {
        'site_id': 'site_id',
        'traffic_limit': 'traffic_limit'
    }

    def __init__(self, site_id=None, traffic_limit=None):
        r"""ScreenRecordsConfigResultReqConfigs

        The model defined in huaweicloud sdk

        :param site_id: 站点ID。
        :type site_id: str
        :param traffic_limit: 录屏限速。
        :type traffic_limit: int
        """
        
        

        self._site_id = None
        self._traffic_limit = None
        self.discriminator = None

        if site_id is not None:
            self.site_id = site_id
        if traffic_limit is not None:
            self.traffic_limit = traffic_limit

    @property
    def site_id(self):
        r"""Gets the site_id of this ScreenRecordsConfigResultReqConfigs.

        站点ID。

        :return: The site_id of this ScreenRecordsConfigResultReqConfigs.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this ScreenRecordsConfigResultReqConfigs.

        站点ID。

        :param site_id: The site_id of this ScreenRecordsConfigResultReqConfigs.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def traffic_limit(self):
        r"""Gets the traffic_limit of this ScreenRecordsConfigResultReqConfigs.

        录屏限速。

        :return: The traffic_limit of this ScreenRecordsConfigResultReqConfigs.
        :rtype: int
        """
        return self._traffic_limit

    @traffic_limit.setter
    def traffic_limit(self, traffic_limit):
        r"""Sets the traffic_limit of this ScreenRecordsConfigResultReqConfigs.

        录屏限速。

        :param traffic_limit: The traffic_limit of this ScreenRecordsConfigResultReqConfigs.
        :type traffic_limit: int
        """
        self._traffic_limit = traffic_limit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScreenRecordsConfigResultReqConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

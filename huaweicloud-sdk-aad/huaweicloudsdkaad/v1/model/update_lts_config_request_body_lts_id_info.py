# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLtsConfigRequestBodyLtsIdInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eps_id': 'str',
        'region': 'str',
        'lts_group_id': 'str',
        'lts_attack_stream_id': 'str'
    }

    attribute_map = {
        'eps_id': 'eps_id',
        'region': 'region',
        'lts_group_id': 'lts_group_id',
        'lts_attack_stream_id': 'lts_attack_stream_id'
    }

    def __init__(self, eps_id=None, region=None, lts_group_id=None, lts_attack_stream_id=None):
        r"""UpdateLtsConfigRequestBodyLtsIdInfo

        The model defined in huaweicloud sdk

        :param eps_id: 企业项目id
        :type eps_id: str
        :param region: region
        :type region: str
        :param lts_group_id: 日志组id
        :type lts_group_id: str
        :param lts_attack_stream_id: 日志流id
        :type lts_attack_stream_id: str
        """
        
        

        self._eps_id = None
        self._region = None
        self._lts_group_id = None
        self._lts_attack_stream_id = None
        self.discriminator = None

        self.eps_id = eps_id
        self.region = region
        self.lts_group_id = lts_group_id
        self.lts_attack_stream_id = lts_attack_stream_id

    @property
    def eps_id(self):
        r"""Gets the eps_id of this UpdateLtsConfigRequestBodyLtsIdInfo.

        企业项目id

        :return: The eps_id of this UpdateLtsConfigRequestBodyLtsIdInfo.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this UpdateLtsConfigRequestBodyLtsIdInfo.

        企业项目id

        :param eps_id: The eps_id of this UpdateLtsConfigRequestBodyLtsIdInfo.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def region(self):
        r"""Gets the region of this UpdateLtsConfigRequestBodyLtsIdInfo.

        region

        :return: The region of this UpdateLtsConfigRequestBodyLtsIdInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this UpdateLtsConfigRequestBodyLtsIdInfo.

        region

        :param region: The region of this UpdateLtsConfigRequestBodyLtsIdInfo.
        :type region: str
        """
        self._region = region

    @property
    def lts_group_id(self):
        r"""Gets the lts_group_id of this UpdateLtsConfigRequestBodyLtsIdInfo.

        日志组id

        :return: The lts_group_id of this UpdateLtsConfigRequestBodyLtsIdInfo.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        r"""Sets the lts_group_id of this UpdateLtsConfigRequestBodyLtsIdInfo.

        日志组id

        :param lts_group_id: The lts_group_id of this UpdateLtsConfigRequestBodyLtsIdInfo.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_attack_stream_id(self):
        r"""Gets the lts_attack_stream_id of this UpdateLtsConfigRequestBodyLtsIdInfo.

        日志流id

        :return: The lts_attack_stream_id of this UpdateLtsConfigRequestBodyLtsIdInfo.
        :rtype: str
        """
        return self._lts_attack_stream_id

    @lts_attack_stream_id.setter
    def lts_attack_stream_id(self, lts_attack_stream_id):
        r"""Sets the lts_attack_stream_id of this UpdateLtsConfigRequestBodyLtsIdInfo.

        日志流id

        :param lts_attack_stream_id: The lts_attack_stream_id of this UpdateLtsConfigRequestBodyLtsIdInfo.
        :type lts_attack_stream_id: str
        """
        self._lts_attack_stream_id = lts_attack_stream_id

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
        if not isinstance(other, UpdateLtsConfigRequestBodyLtsIdInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

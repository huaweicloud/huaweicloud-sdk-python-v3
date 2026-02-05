# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberGroupUrlInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'member_group_id': 'str',
        'req_protocol': 'str',
        'req_method': 'str',
        'req_uri': 'str'
    }

    attribute_map = {
        'member_group_id': 'member_group_id',
        'req_protocol': 'req_protocol',
        'req_method': 'req_method',
        'req_uri': 'req_uri'
    }

    def __init__(self, member_group_id=None, req_protocol=None, req_method=None, req_uri=None):
        r"""MemberGroupUrlInfo

        The model defined in huaweicloud sdk

        :param member_group_id: 后端服务器分组ID。
        :type member_group_id: str
        :param req_protocol: 请求协议。
        :type req_protocol: str
        :param req_method: 请求方式。
        :type req_method: str
        :param req_uri: 请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512字符，且满足URI规范。 支持环境变量，使用环境变量时，每个变量名的长度为3~32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 &gt; 需要服从URI规范。 
        :type req_uri: str
        """
        
        

        self._member_group_id = None
        self._req_protocol = None
        self._req_method = None
        self._req_uri = None
        self.discriminator = None

        self.member_group_id = member_group_id
        self.req_protocol = req_protocol
        self.req_method = req_method
        self.req_uri = req_uri

    @property
    def member_group_id(self):
        r"""Gets the member_group_id of this MemberGroupUrlInfo.

        后端服务器分组ID。

        :return: The member_group_id of this MemberGroupUrlInfo.
        :rtype: str
        """
        return self._member_group_id

    @member_group_id.setter
    def member_group_id(self, member_group_id):
        r"""Sets the member_group_id of this MemberGroupUrlInfo.

        后端服务器分组ID。

        :param member_group_id: The member_group_id of this MemberGroupUrlInfo.
        :type member_group_id: str
        """
        self._member_group_id = member_group_id

    @property
    def req_protocol(self):
        r"""Gets the req_protocol of this MemberGroupUrlInfo.

        请求协议。

        :return: The req_protocol of this MemberGroupUrlInfo.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        r"""Sets the req_protocol of this MemberGroupUrlInfo.

        请求协议。

        :param req_protocol: The req_protocol of this MemberGroupUrlInfo.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

    @property
    def req_method(self):
        r"""Gets the req_method of this MemberGroupUrlInfo.

        请求方式。

        :return: The req_method of this MemberGroupUrlInfo.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        r"""Sets the req_method of this MemberGroupUrlInfo.

        请求方式。

        :param req_method: The req_method of this MemberGroupUrlInfo.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        r"""Gets the req_uri of this MemberGroupUrlInfo.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512字符，且满足URI规范。 支持环境变量，使用环境变量时，每个变量名的长度为3~32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 > 需要服从URI规范。 

        :return: The req_uri of this MemberGroupUrlInfo.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        r"""Sets the req_uri of this MemberGroupUrlInfo.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512字符，且满足URI规范。 支持环境变量，使用环境变量时，每个变量名的长度为3~32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 > 需要服从URI规范。 

        :param req_uri: The req_uri of this MemberGroupUrlInfo.
        :type req_uri: str
        """
        self._req_uri = req_uri

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
        if not isinstance(other, MemberGroupUrlInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

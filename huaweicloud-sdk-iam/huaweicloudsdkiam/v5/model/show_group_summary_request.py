# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupSummaryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'user_id': 'user_id'
    }

    def __init__(self, limit=None, marker=None, user_id=None):
        r"""ShowGroupSummaryRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量，范围为1到200条，默认为100条。
        :type limit: int
        :param marker: 分页标记，长度为4到400个字符，只包含字母、数字、\&quot;+\&quot;、\&quot;/\&quot;、\&quot;&#x3D;\&quot;、\&quot;-\&quot;和\&quot;_\&quot;的字符串。
        :type marker: str
        :param user_id: IAM用户ID。
        :type user_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._user_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if user_id is not None:
            self.user_id = user_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowGroupSummaryRequest.

        每页显示的条目数量，范围为1到200条，默认为100条。

        :return: The limit of this ShowGroupSummaryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowGroupSummaryRequest.

        每页显示的条目数量，范围为1到200条，默认为100条。

        :param limit: The limit of this ShowGroupSummaryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ShowGroupSummaryRequest.

        分页标记，长度为4到400个字符，只包含字母、数字、\"+\"、\"/\"、\"=\"、\"-\"和\"_\"的字符串。

        :return: The marker of this ShowGroupSummaryRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ShowGroupSummaryRequest.

        分页标记，长度为4到400个字符，只包含字母、数字、\"+\"、\"/\"、\"=\"、\"-\"和\"_\"的字符串。

        :param marker: The marker of this ShowGroupSummaryRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowGroupSummaryRequest.

        IAM用户ID。

        :return: The user_id of this ShowGroupSummaryRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowGroupSummaryRequest.

        IAM用户ID。

        :param user_id: The user_id of this ShowGroupSummaryRequest.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, ShowGroupSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

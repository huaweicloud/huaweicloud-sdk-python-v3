# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTtscVocabularyGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'x_app_user_id': 'str',
        'group_id': 'str',
        'body': 'SaveTtscVocabularyGroupsRequestBody'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'x_app_user_id': 'X-App-UserId',
        'group_id': 'group_id',
        'body': 'body'
    }

    def __init__(self, x_request_id=None, x_app_user_id=None, group_id=None, body=None):
        r"""UpdateTtscVocabularyGroupsRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成
        :type x_request_id: str
        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param group_id: 分组id
        :type group_id: str
        :param body: Body of the UpdateTtscVocabularyGroupsRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.SaveTtscVocabularyGroupsRequestBody`
        """
        
        

        self._x_request_id = None
        self._x_app_user_id = None
        self._group_id = None
        self._body = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.group_id = group_id
        if body is not None:
            self.body = body

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateTtscVocabularyGroupsRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成

        :return: The x_request_id of this UpdateTtscVocabularyGroupsRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateTtscVocabularyGroupsRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成

        :param x_request_id: The x_request_id of this UpdateTtscVocabularyGroupsRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this UpdateTtscVocabularyGroupsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this UpdateTtscVocabularyGroupsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this UpdateTtscVocabularyGroupsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this UpdateTtscVocabularyGroupsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateTtscVocabularyGroupsRequest.

        分组id

        :return: The group_id of this UpdateTtscVocabularyGroupsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateTtscVocabularyGroupsRequest.

        分组id

        :param group_id: The group_id of this UpdateTtscVocabularyGroupsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def body(self):
        r"""Gets the body of this UpdateTtscVocabularyGroupsRequest.

        :return: The body of this UpdateTtscVocabularyGroupsRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SaveTtscVocabularyGroupsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTtscVocabularyGroupsRequest.

        :param body: The body of this UpdateTtscVocabularyGroupsRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.SaveTtscVocabularyGroupsRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateTtscVocabularyGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

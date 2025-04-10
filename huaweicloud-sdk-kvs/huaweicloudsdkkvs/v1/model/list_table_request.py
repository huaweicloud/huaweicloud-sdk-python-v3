# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'store_name': 'str',
        'body': 'ListTableRequestBody'
    }

    attribute_map = {
        'store_name': 'store_name',
        'body': 'body'
    }

    def __init__(self, store_name=None, body=None):
        r"""ListTableRequest

        The model defined in huaweicloud sdk

        :param store_name: 仓名，全域唯一，不同租户的仓名不能相同。  - 格式：${prefix}-${region-code}-${account-id}，其中prefix为自定义前缀，region-code为kvs集群所在的区域代码，account-id为用户的账户id - 取值字符限制：[a-z0-9-]+ - 长度：[16,52] &gt; \&quot;-\&quot;不能出现在名字头部或尾部
        :type store_name: str
        :param body: Body of the ListTableRequest
        :type body: :class:`huaweicloudsdkkvs.v1.ListTableRequestBody`
        """
        
        

        self._store_name = None
        self._body = None
        self.discriminator = None

        if store_name is not None:
            self.store_name = store_name
        if body is not None:
            self.body = body

    @property
    def store_name(self):
        r"""Gets the store_name of this ListTableRequest.

        仓名，全域唯一，不同租户的仓名不能相同。  - 格式：${prefix}-${region-code}-${account-id}，其中prefix为自定义前缀，region-code为kvs集群所在的区域代码，account-id为用户的账户id - 取值字符限制：[a-z0-9-]+ - 长度：[16,52] > \"-\"不能出现在名字头部或尾部

        :return: The store_name of this ListTableRequest.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this ListTableRequest.

        仓名，全域唯一，不同租户的仓名不能相同。  - 格式：${prefix}-${region-code}-${account-id}，其中prefix为自定义前缀，region-code为kvs集群所在的区域代码，account-id为用户的账户id - 取值字符限制：[a-z0-9-]+ - 长度：[16,52] > \"-\"不能出现在名字头部或尾部

        :param store_name: The store_name of this ListTableRequest.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def body(self):
        r"""Gets the body of this ListTableRequest.

        :return: The body of this ListTableRequest.
        :rtype: :class:`huaweicloudsdkkvs.v1.ListTableRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListTableRequest.

        :param body: The body of this ListTableRequest.
        :type body: :class:`huaweicloudsdkkvs.v1.ListTableRequestBody`
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
        if not isinstance(other, ListTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

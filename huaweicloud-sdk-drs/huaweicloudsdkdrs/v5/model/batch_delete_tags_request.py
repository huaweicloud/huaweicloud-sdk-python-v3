# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'x_language': 'str',
        'resource_id': 'str',
        'body': 'BatchDeleteTagReq'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'x_language': 'X-Language',
        'resource_id': 'resource_id',
        'body': 'body'
    }

    def __init__(self, resource_type=None, x_language=None, resource_id=None, body=None):
        """BatchDeleteTagsRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型。 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - subscription：数据订阅 - backupMigration：备份迁移 - replay：录制回放
        :type resource_type: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param resource_id: 资源ID，即DRS任务ID。
        :type resource_id: str
        :param body: Body of the BatchDeleteTagsRequest
        :type body: :class:`huaweicloudsdkdrs.v5.BatchDeleteTagReq`
        """
        
        

        self._resource_type = None
        self._x_language = None
        self._resource_id = None
        self._body = None
        self.discriminator = None

        self.resource_type = resource_type
        if x_language is not None:
            self.x_language = x_language
        self.resource_id = resource_id
        if body is not None:
            self.body = body

    @property
    def resource_type(self):
        """Gets the resource_type of this BatchDeleteTagsRequest.

        资源类型。 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - subscription：数据订阅 - backupMigration：备份迁移 - replay：录制回放

        :return: The resource_type of this BatchDeleteTagsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BatchDeleteTagsRequest.

        资源类型。 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - subscription：数据订阅 - backupMigration：备份迁移 - replay：录制回放

        :param resource_type: The resource_type of this BatchDeleteTagsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def x_language(self):
        """Gets the x_language of this BatchDeleteTagsRequest.

        请求语言类型。

        :return: The x_language of this BatchDeleteTagsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this BatchDeleteTagsRequest.

        请求语言类型。

        :param x_language: The x_language of this BatchDeleteTagsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def resource_id(self):
        """Gets the resource_id of this BatchDeleteTagsRequest.

        资源ID，即DRS任务ID。

        :return: The resource_id of this BatchDeleteTagsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BatchDeleteTagsRequest.

        资源ID，即DRS任务ID。

        :param resource_id: The resource_id of this BatchDeleteTagsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def body(self):
        """Gets the body of this BatchDeleteTagsRequest.

        :return: The body of this BatchDeleteTagsRequest.
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchDeleteTagReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchDeleteTagsRequest.

        :param body: The body of this BatchDeleteTagsRequest.
        :type body: :class:`huaweicloudsdkdrs.v5.BatchDeleteTagReq`
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
        if not isinstance(other, BatchDeleteTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

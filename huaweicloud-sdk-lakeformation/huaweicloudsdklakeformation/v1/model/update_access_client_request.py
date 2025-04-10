# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAccessClientRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'client_id': 'str',
        'body': 'UpdateAccessClientRequestBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'client_id': 'client_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, client_id=None, body=None):
        r"""UpdateAccessClientRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param client_id: 客户端ID。创建客户端时自动生成。
        :type client_id: str
        :param body: Body of the UpdateAccessClientRequest
        :type body: :class:`huaweicloudsdklakeformation.v1.UpdateAccessClientRequestBody`
        """
        
        

        self._instance_id = None
        self._client_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.client_id = client_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateAccessClientRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this UpdateAccessClientRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateAccessClientRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this UpdateAccessClientRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def client_id(self):
        r"""Gets the client_id of this UpdateAccessClientRequest.

        客户端ID。创建客户端时自动生成。

        :return: The client_id of this UpdateAccessClientRequest.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this UpdateAccessClientRequest.

        客户端ID。创建客户端时自动生成。

        :param client_id: The client_id of this UpdateAccessClientRequest.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def body(self):
        r"""Gets the body of this UpdateAccessClientRequest.

        :return: The body of this UpdateAccessClientRequest.
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateAccessClientRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAccessClientRequest.

        :param body: The body of this UpdateAccessClientRequest.
        :type body: :class:`huaweicloudsdklakeformation.v1.UpdateAccessClientRequestBody`
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
        if not isinstance(other, UpdateAccessClientRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

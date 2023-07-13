# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportApiDefinitionsV2Request:

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
        'oas_version': 'str',
        'body': 'ExportOpenApiReq'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'oas_version': 'oas_version',
        'body': 'body'
    }

    def __init__(self, instance_id=None, oas_version=None, body=None):
        """ExportApiDefinitionsV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param oas_version: OpenAPI版本
        :type oas_version: str
        :param body: Body of the ExportApiDefinitionsV2Request
        :type body: :class:`huaweicloudsdkapig.v2.ExportOpenApiReq`
        """
        
        

        self._instance_id = None
        self._oas_version = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        if oas_version is not None:
            self.oas_version = oas_version
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this ExportApiDefinitionsV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ExportApiDefinitionsV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ExportApiDefinitionsV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ExportApiDefinitionsV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def oas_version(self):
        """Gets the oas_version of this ExportApiDefinitionsV2Request.

        OpenAPI版本

        :return: The oas_version of this ExportApiDefinitionsV2Request.
        :rtype: str
        """
        return self._oas_version

    @oas_version.setter
    def oas_version(self, oas_version):
        """Sets the oas_version of this ExportApiDefinitionsV2Request.

        OpenAPI版本

        :param oas_version: The oas_version of this ExportApiDefinitionsV2Request.
        :type oas_version: str
        """
        self._oas_version = oas_version

    @property
    def body(self):
        """Gets the body of this ExportApiDefinitionsV2Request.

        :return: The body of this ExportApiDefinitionsV2Request.
        :rtype: :class:`huaweicloudsdkapig.v2.ExportOpenApiReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ExportApiDefinitionsV2Request.

        :param body: The body of this ExportApiDefinitionsV2Request.
        :type body: :class:`huaweicloudsdkapig.v2.ExportOpenApiReq`
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
        if not isinstance(other, ExportApiDefinitionsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

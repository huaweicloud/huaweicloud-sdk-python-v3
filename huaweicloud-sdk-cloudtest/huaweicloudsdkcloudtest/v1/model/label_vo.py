# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'region': 'str',
        'label_name': 'str',
        'service_type': 'str',
        'resource_type': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'region': 'region',
        'label_name': 'label_name',
        'service_type': 'service_type',
        'resource_type': 'resource_type',
        'project_id': 'project_id'
    }

    def __init__(self, uri=None, region=None, label_name=None, service_type=None, resource_type=None, project_id=None):
        r"""LabelVo

        The model defined in huaweicloud sdk

        :param uri: uri主键
        :type uri: str
        :param region: 逻辑region
        :type region: str
        :param label_name: 标签名称
        :type label_name: str
        :param service_type: 服务类型
        :type service_type: str
        :param resource_type: 所属资源类型（TestCase：用例，Task：测试套）
        :type resource_type: str
        :param project_id: 项目ID
        :type project_id: str
        """
        
        

        self._uri = None
        self._region = None
        self._label_name = None
        self._service_type = None
        self._resource_type = None
        self._project_id = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if region is not None:
            self.region = region
        if label_name is not None:
            self.label_name = label_name
        if service_type is not None:
            self.service_type = service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if project_id is not None:
            self.project_id = project_id

    @property
    def uri(self):
        r"""Gets the uri of this LabelVo.

        uri主键

        :return: The uri of this LabelVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this LabelVo.

        uri主键

        :param uri: The uri of this LabelVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def region(self):
        r"""Gets the region of this LabelVo.

        逻辑region

        :return: The region of this LabelVo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this LabelVo.

        逻辑region

        :param region: The region of this LabelVo.
        :type region: str
        """
        self._region = region

    @property
    def label_name(self):
        r"""Gets the label_name of this LabelVo.

        标签名称

        :return: The label_name of this LabelVo.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        r"""Sets the label_name of this LabelVo.

        标签名称

        :param label_name: The label_name of this LabelVo.
        :type label_name: str
        """
        self._label_name = label_name

    @property
    def service_type(self):
        r"""Gets the service_type of this LabelVo.

        服务类型

        :return: The service_type of this LabelVo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this LabelVo.

        服务类型

        :param service_type: The service_type of this LabelVo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this LabelVo.

        所属资源类型（TestCase：用例，Task：测试套）

        :return: The resource_type of this LabelVo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this LabelVo.

        所属资源类型（TestCase：用例，Task：测试套）

        :param resource_type: The resource_type of this LabelVo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def project_id(self):
        r"""Gets the project_id of this LabelVo.

        项目ID

        :return: The project_id of this LabelVo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this LabelVo.

        项目ID

        :param project_id: The project_id of this LabelVo.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, LabelVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssociatedResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'associated_resources': 'list[AssociatedResourceListResponse]',
        'errors': 'list[ResourceErrorListResponse]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'associated_resources': 'associated_resources',
        'errors': 'errors'
    }

    def __init__(self, id=None, name=None, type=None, associated_resources=None, errors=None):
        r"""ShowAssociatedResourcesResponse

        The model defined in huaweicloud sdk

        :param id: 资源ID
        :type id: str
        :param name: 资源名称
        :type name: str
        :param type: 关联的资源类型
        :type type: str
        :param associated_resources: 关联资源列表
        :type associated_resources: list[:class:`huaweicloudsdkeps.v1.AssociatedResourceListResponse`]
        :param errors: 错误信息列表
        :type errors: list[:class:`huaweicloudsdkeps.v1.ResourceErrorListResponse`]
        """
        
        super(ShowAssociatedResourcesResponse, self).__init__()

        self._id = None
        self._name = None
        self._type = None
        self._associated_resources = None
        self._errors = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if associated_resources is not None:
            self.associated_resources = associated_resources
        if errors is not None:
            self.errors = errors

    @property
    def id(self):
        r"""Gets the id of this ShowAssociatedResourcesResponse.

        资源ID

        :return: The id of this ShowAssociatedResourcesResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAssociatedResourcesResponse.

        资源ID

        :param id: The id of this ShowAssociatedResourcesResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowAssociatedResourcesResponse.

        资源名称

        :return: The name of this ShowAssociatedResourcesResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAssociatedResourcesResponse.

        资源名称

        :param name: The name of this ShowAssociatedResourcesResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ShowAssociatedResourcesResponse.

        关联的资源类型

        :return: The type of this ShowAssociatedResourcesResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowAssociatedResourcesResponse.

        关联的资源类型

        :param type: The type of this ShowAssociatedResourcesResponse.
        :type type: str
        """
        self._type = type

    @property
    def associated_resources(self):
        r"""Gets the associated_resources of this ShowAssociatedResourcesResponse.

        关联资源列表

        :return: The associated_resources of this ShowAssociatedResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkeps.v1.AssociatedResourceListResponse`]
        """
        return self._associated_resources

    @associated_resources.setter
    def associated_resources(self, associated_resources):
        r"""Sets the associated_resources of this ShowAssociatedResourcesResponse.

        关联资源列表

        :param associated_resources: The associated_resources of this ShowAssociatedResourcesResponse.
        :type associated_resources: list[:class:`huaweicloudsdkeps.v1.AssociatedResourceListResponse`]
        """
        self._associated_resources = associated_resources

    @property
    def errors(self):
        r"""Gets the errors of this ShowAssociatedResourcesResponse.

        错误信息列表

        :return: The errors of this ShowAssociatedResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkeps.v1.ResourceErrorListResponse`]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        r"""Sets the errors of this ShowAssociatedResourcesResponse.

        错误信息列表

        :param errors: The errors of this ShowAssociatedResourcesResponse.
        :type errors: list[:class:`huaweicloudsdkeps.v1.ResourceErrorListResponse`]
        """
        self._errors = errors

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
        if not isinstance(other, ShowAssociatedResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

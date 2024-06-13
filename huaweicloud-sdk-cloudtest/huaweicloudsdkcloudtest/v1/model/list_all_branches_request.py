# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllBranchesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'sort_field': 'str',
        'sort_type': 'str'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type'
    }

    def __init__(self, project_uuid=None, sort_field=None, sort_type=None):
        """ListAllBranchesRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目ID（云龙场景，传入微服务ID）
        :type project_uuid: str
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_type: 排序方式
        :type sort_type: str
        """
        
        

        self._project_uuid = None
        self._sort_field = None
        self._sort_type = None
        self.discriminator = None

        self.project_uuid = project_uuid
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type

    @property
    def project_uuid(self):
        """Gets the project_uuid of this ListAllBranchesRequest.

        项目ID（云龙场景，传入微服务ID）

        :return: The project_uuid of this ListAllBranchesRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this ListAllBranchesRequest.

        项目ID（云龙场景，传入微服务ID）

        :param project_uuid: The project_uuid of this ListAllBranchesRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def sort_field(self):
        """Gets the sort_field of this ListAllBranchesRequest.

        排序字段

        :return: The sort_field of this ListAllBranchesRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ListAllBranchesRequest.

        排序字段

        :param sort_field: The sort_field of this ListAllBranchesRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        """Gets the sort_type of this ListAllBranchesRequest.

        排序方式

        :return: The sort_type of this ListAllBranchesRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this ListAllBranchesRequest.

        排序方式

        :param sort_type: The sort_type of this ListAllBranchesRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

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
        if not isinstance(other, ListAllBranchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

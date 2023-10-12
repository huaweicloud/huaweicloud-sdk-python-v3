# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApicInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dlm_type': 'str',
        'apig_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'apig_type': 'apig_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, dlm_type=None, apig_type=None, limit=None, offset=None):
        """ListApicInstancesRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param dlm_type: dlm版本类型
        :type dlm_type: str
        :param apig_type: 网关类型
        :type apig_type: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._apig_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        self.dlm_type = dlm_type
        self.apig_type = apig_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this ListApicInstancesRequest.

        工作空间id

        :return: The workspace of this ListApicInstancesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListApicInstancesRequest.

        工作空间id

        :param workspace: The workspace of this ListApicInstancesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        """Gets the dlm_type of this ListApicInstancesRequest.

        dlm版本类型

        :return: The dlm_type of this ListApicInstancesRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        """Sets the dlm_type of this ListApicInstancesRequest.

        dlm版本类型

        :param dlm_type: The dlm_type of this ListApicInstancesRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def apig_type(self):
        """Gets the apig_type of this ListApicInstancesRequest.

        网关类型

        :return: The apig_type of this ListApicInstancesRequest.
        :rtype: str
        """
        return self._apig_type

    @apig_type.setter
    def apig_type(self, apig_type):
        """Sets the apig_type of this ListApicInstancesRequest.

        网关类型

        :param apig_type: The apig_type of this ListApicInstancesRequest.
        :type apig_type: str
        """
        self._apig_type = apig_type

    @property
    def limit(self):
        """Gets the limit of this ListApicInstancesRequest.

        limit

        :return: The limit of this ListApicInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApicInstancesRequest.

        limit

        :param limit: The limit of this ListApicInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListApicInstancesRequest.

        offset

        :return: The offset of this ListApicInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListApicInstancesRequest.

        offset

        :param offset: The offset of this ListApicInstancesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListApicInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

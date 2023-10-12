# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApplyDetailRequest:

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
        'apply_id': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'apply_id': 'apply_id'
    }

    def __init__(self, workspace=None, dlm_type=None, apply_id=None):
        """ShowApplyDetailRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param dlm_type: dlm版本类型
        :type dlm_type: str
        :param apply_id: 审核信息id
        :type apply_id: str
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._apply_id = None
        self.discriminator = None

        self.workspace = workspace
        self.dlm_type = dlm_type
        self.apply_id = apply_id

    @property
    def workspace(self):
        """Gets the workspace of this ShowApplyDetailRequest.

        工作空间id

        :return: The workspace of this ShowApplyDetailRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowApplyDetailRequest.

        工作空间id

        :param workspace: The workspace of this ShowApplyDetailRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        """Gets the dlm_type of this ShowApplyDetailRequest.

        dlm版本类型

        :return: The dlm_type of this ShowApplyDetailRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        """Sets the dlm_type of this ShowApplyDetailRequest.

        dlm版本类型

        :param dlm_type: The dlm_type of this ShowApplyDetailRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def apply_id(self):
        """Gets the apply_id of this ShowApplyDetailRequest.

        审核信息id

        :return: The apply_id of this ShowApplyDetailRequest.
        :rtype: str
        """
        return self._apply_id

    @apply_id.setter
    def apply_id(self, apply_id):
        """Sets the apply_id of this ShowApplyDetailRequest.

        审核信息id

        :param apply_id: The apply_id of this ShowApplyDetailRequest.
        :type apply_id: str
        """
        self._apply_id = apply_id

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
        if not isinstance(other, ShowApplyDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

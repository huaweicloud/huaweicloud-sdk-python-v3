# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateSecurityLevelToEntitieRequest:

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
        'guid': 'str',
        'security_level': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'guid': 'guid',
        'security_level': 'security-level'
    }

    def __init__(self, workspace=None, guid=None, security_level=None):
        r"""AssociateSecurityLevelToEntitieRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param guid: 资产id
        :type guid: str
        :param security_level: 资产密级
        :type security_level: str
        """
        
        

        self._workspace = None
        self._guid = None
        self._security_level = None
        self.discriminator = None

        self.workspace = workspace
        self.guid = guid
        self.security_level = security_level

    @property
    def workspace(self):
        r"""Gets the workspace of this AssociateSecurityLevelToEntitieRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this AssociateSecurityLevelToEntitieRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this AssociateSecurityLevelToEntitieRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this AssociateSecurityLevelToEntitieRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def guid(self):
        r"""Gets the guid of this AssociateSecurityLevelToEntitieRequest.

        资产id

        :return: The guid of this AssociateSecurityLevelToEntitieRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this AssociateSecurityLevelToEntitieRequest.

        资产id

        :param guid: The guid of this AssociateSecurityLevelToEntitieRequest.
        :type guid: str
        """
        self._guid = guid

    @property
    def security_level(self):
        r"""Gets the security_level of this AssociateSecurityLevelToEntitieRequest.

        资产密级

        :return: The security_level of this AssociateSecurityLevelToEntitieRequest.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this AssociateSecurityLevelToEntitieRequest.

        资产密级

        :param security_level: The security_level of this AssociateSecurityLevelToEntitieRequest.
        :type security_level: str
        """
        self._security_level = security_level

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
        if not isinstance(other, AssociateSecurityLevelToEntitieRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentPatchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'patch': 'Patch'
    }

    attribute_map = {
        'version': 'version',
        'patch': 'patch'
    }

    def __init__(self, version=None, patch=None):
        r"""DeploymentPatchRequest

        The model defined in huaweicloud sdk

        :param version: 技能版本，可选，当下发的技能版本和当前部署的版本不一致的时候，根据技能模板参数更新部署
        :type version: str
        :param patch: 
        :type patch: :class:`huaweicloudsdkhilens.v3.Patch`
        """
        
        

        self._version = None
        self._patch = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if patch is not None:
            self.patch = patch

    @property
    def version(self):
        r"""Gets the version of this DeploymentPatchRequest.

        技能版本，可选，当下发的技能版本和当前部署的版本不一致的时候，根据技能模板参数更新部署

        :return: The version of this DeploymentPatchRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DeploymentPatchRequest.

        技能版本，可选，当下发的技能版本和当前部署的版本不一致的时候，根据技能模板参数更新部署

        :param version: The version of this DeploymentPatchRequest.
        :type version: str
        """
        self._version = version

    @property
    def patch(self):
        r"""Gets the patch of this DeploymentPatchRequest.

        :return: The patch of this DeploymentPatchRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.Patch`
        """
        return self._patch

    @patch.setter
    def patch(self, patch):
        r"""Sets the patch of this DeploymentPatchRequest.

        :param patch: The patch of this DeploymentPatchRequest.
        :type patch: :class:`huaweicloudsdkhilens.v3.Patch`
        """
        self._patch = patch

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
        if not isinstance(other, DeploymentPatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

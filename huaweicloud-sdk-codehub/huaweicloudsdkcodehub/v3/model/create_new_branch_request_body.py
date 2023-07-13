# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNewBranchRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch_name': 'str',
        'ref': 'str'
    }

    attribute_map = {
        'branch_name': 'branch_name',
        'ref': 'ref'
    }

    def __init__(self, branch_name=None, ref=None):
        """CreateNewBranchRequestBody

        The model defined in huaweicloud sdk

        :param branch_name: 分支名称
        :type branch_name: str
        :param ref: 源分支名称
        :type ref: str
        """
        
        

        self._branch_name = None
        self._ref = None
        self.discriminator = None

        self.branch_name = branch_name
        self.ref = ref

    @property
    def branch_name(self):
        """Gets the branch_name of this CreateNewBranchRequestBody.

        分支名称

        :return: The branch_name of this CreateNewBranchRequestBody.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this CreateNewBranchRequestBody.

        分支名称

        :param branch_name: The branch_name of this CreateNewBranchRequestBody.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def ref(self):
        """Gets the ref of this CreateNewBranchRequestBody.

        源分支名称

        :return: The ref of this CreateNewBranchRequestBody.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this CreateNewBranchRequestBody.

        源分支名称

        :param ref: The ref of this CreateNewBranchRequestBody.
        :type ref: str
        """
        self._ref = ref

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
        if not isinstance(other, CreateNewBranchRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

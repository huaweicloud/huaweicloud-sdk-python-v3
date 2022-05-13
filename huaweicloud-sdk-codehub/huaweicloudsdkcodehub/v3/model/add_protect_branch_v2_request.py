# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddProtectBranchV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'branch_name': 'str',
        'body': 'AddProtectRequest'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'branch_name': 'branch_name',
        'body': 'body'
    }

    def __init__(self, repository_id=None, branch_name=None, body=None):
        """AddProtectBranchV2Request

        The model defined in huaweicloud sdk

        :param repository_id: 仓库主键id
        :type repository_id: int
        :param branch_name: 分支名称
        :type branch_name: str
        :param body: Body of the AddProtectBranchV2Request
        :type body: :class:`huaweicloudsdkcodehub.v3.AddProtectRequest`
        """
        
        

        self._repository_id = None
        self._branch_name = None
        self._body = None
        self.discriminator = None

        self.repository_id = repository_id
        self.branch_name = branch_name
        if body is not None:
            self.body = body

    @property
    def repository_id(self):
        """Gets the repository_id of this AddProtectBranchV2Request.

        仓库主键id

        :return: The repository_id of this AddProtectBranchV2Request.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this AddProtectBranchV2Request.

        仓库主键id

        :param repository_id: The repository_id of this AddProtectBranchV2Request.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def branch_name(self):
        """Gets the branch_name of this AddProtectBranchV2Request.

        分支名称

        :return: The branch_name of this AddProtectBranchV2Request.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this AddProtectBranchV2Request.

        分支名称

        :param branch_name: The branch_name of this AddProtectBranchV2Request.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def body(self):
        """Gets the body of this AddProtectBranchV2Request.


        :return: The body of this AddProtectBranchV2Request.
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddProtectRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AddProtectBranchV2Request.


        :param body: The body of this AddProtectBranchV2Request.
        :type body: :class:`huaweicloudsdkcodehub.v3.AddProtectRequest`
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
        if not isinstance(other, AddProtectBranchV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

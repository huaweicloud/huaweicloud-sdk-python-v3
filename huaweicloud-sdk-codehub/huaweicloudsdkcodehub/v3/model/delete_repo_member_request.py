# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRepoMemberRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'member_id': 'str',
        'repository_uuid': 'str'
    }

    attribute_map = {
        'member_id': 'member_id',
        'repository_uuid': 'repository_uuid'
    }

    def __init__(self, member_id=None, repository_uuid=None):
        r"""DeleteRepoMemberRequest

        The model defined in huaweicloud sdk

        :param member_id: 仓库成员id
        :type member_id: str
        :param repository_uuid: 仓库uuid(由CreateRepository接口返回)
        :type repository_uuid: str
        """
        
        

        self._member_id = None
        self._repository_uuid = None
        self.discriminator = None

        self.member_id = member_id
        self.repository_uuid = repository_uuid

    @property
    def member_id(self):
        r"""Gets the member_id of this DeleteRepoMemberRequest.

        仓库成员id

        :return: The member_id of this DeleteRepoMemberRequest.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        r"""Sets the member_id of this DeleteRepoMemberRequest.

        仓库成员id

        :param member_id: The member_id of this DeleteRepoMemberRequest.
        :type member_id: str
        """
        self._member_id = member_id

    @property
    def repository_uuid(self):
        r"""Gets the repository_uuid of this DeleteRepoMemberRequest.

        仓库uuid(由CreateRepository接口返回)

        :return: The repository_uuid of this DeleteRepoMemberRequest.
        :rtype: str
        """
        return self._repository_uuid

    @repository_uuid.setter
    def repository_uuid(self, repository_uuid):
        r"""Sets the repository_uuid of this DeleteRepoMemberRequest.

        仓库uuid(由CreateRepository接口返回)

        :param repository_uuid: The repository_uuid of this DeleteRepoMemberRequest.
        :type repository_uuid: str
        """
        self._repository_uuid = repository_uuid

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
        if not isinstance(other, DeleteRepoMemberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

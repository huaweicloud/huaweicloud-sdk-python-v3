# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLastPushEventInRepositoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ref': 'str',
        'created_at': 'str',
        'repository': 'RepositoryBriefDto'
    }

    attribute_map = {
        'ref': 'ref',
        'created_at': 'created_at',
        'repository': 'repository'
    }

    def __init__(self, ref=None, created_at=None, repository=None):
        r"""ShowLastPushEventInRepositoryResponse

        The model defined in huaweicloud sdk

        :param ref: **参数解释：** 分支或者tag名称。 **取值范围：** 不涉及。
        :type ref: str
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 不涉及。
        :type created_at: str
        :param repository: 
        :type repository: :class:`huaweicloudsdkcodehub.v4.RepositoryBriefDto`
        """
        
        super(ShowLastPushEventInRepositoryResponse, self).__init__()

        self._ref = None
        self._created_at = None
        self._repository = None
        self.discriminator = None

        if ref is not None:
            self.ref = ref
        if created_at is not None:
            self.created_at = created_at
        if repository is not None:
            self.repository = repository

    @property
    def ref(self):
        r"""Gets the ref of this ShowLastPushEventInRepositoryResponse.

        **参数解释：** 分支或者tag名称。 **取值范围：** 不涉及。

        :return: The ref of this ShowLastPushEventInRepositoryResponse.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this ShowLastPushEventInRepositoryResponse.

        **参数解释：** 分支或者tag名称。 **取值范围：** 不涉及。

        :param ref: The ref of this ShowLastPushEventInRepositoryResponse.
        :type ref: str
        """
        self._ref = ref

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowLastPushEventInRepositoryResponse.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :return: The created_at of this ShowLastPushEventInRepositoryResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowLastPushEventInRepositoryResponse.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :param created_at: The created_at of this ShowLastPushEventInRepositoryResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def repository(self):
        r"""Gets the repository of this ShowLastPushEventInRepositoryResponse.

        :return: The repository of this ShowLastPushEventInRepositoryResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepositoryBriefDto`
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this ShowLastPushEventInRepositoryResponse.

        :param repository: The repository of this ShowLastPushEventInRepositoryResponse.
        :type repository: :class:`huaweicloudsdkcodehub.v4.RepositoryBriefDto`
        """
        self._repository = repository

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
        if not isinstance(other, ShowLastPushEventInRepositoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

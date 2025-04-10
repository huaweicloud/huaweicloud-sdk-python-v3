# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMavenInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'policy': 'str',
        'access': 'str',
        'default': 'str',
        'ids': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'policy': 'policy',
        'access': 'access',
        'default': 'default',
        'ids': 'ids'
    }

    def __init__(self, project_id=None, policy=None, access=None, default=None, ids=None):
        r"""ShowMavenInfoRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param policy: snapshot or releases
        :type policy: str
        :param access: r or rw
        :type access: str
        :param default: 是否返回默认仓库 true or false
        :type default: str
        :param ids: 仓库id 多个仓库id用英文逗号间隔
        :type ids: str
        """
        
        

        self._project_id = None
        self._policy = None
        self._access = None
        self._default = None
        self._ids = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if policy is not None:
            self.policy = policy
        if access is not None:
            self.access = access
        if default is not None:
            self.default = default
        if ids is not None:
            self.ids = ids

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowMavenInfoRequest.

        项目id

        :return: The project_id of this ShowMavenInfoRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowMavenInfoRequest.

        项目id

        :param project_id: The project_id of this ShowMavenInfoRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def policy(self):
        r"""Gets the policy of this ShowMavenInfoRequest.

        snapshot or releases

        :return: The policy of this ShowMavenInfoRequest.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ShowMavenInfoRequest.

        snapshot or releases

        :param policy: The policy of this ShowMavenInfoRequest.
        :type policy: str
        """
        self._policy = policy

    @property
    def access(self):
        r"""Gets the access of this ShowMavenInfoRequest.

        r or rw

        :return: The access of this ShowMavenInfoRequest.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        r"""Sets the access of this ShowMavenInfoRequest.

        r or rw

        :param access: The access of this ShowMavenInfoRequest.
        :type access: str
        """
        self._access = access

    @property
    def default(self):
        r"""Gets the default of this ShowMavenInfoRequest.

        是否返回默认仓库 true or false

        :return: The default of this ShowMavenInfoRequest.
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this ShowMavenInfoRequest.

        是否返回默认仓库 true or false

        :param default: The default of this ShowMavenInfoRequest.
        :type default: str
        """
        self._default = default

    @property
    def ids(self):
        r"""Gets the ids of this ShowMavenInfoRequest.

        仓库id 多个仓库id用英文逗号间隔

        :return: The ids of this ShowMavenInfoRequest.
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ShowMavenInfoRequest.

        仓库id 多个仓库id用英文逗号间隔

        :param ids: The ids of this ShowMavenInfoRequest.
        :type ids: str
        """
        self._ids = ids

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
        if not isinstance(other, ShowMavenInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

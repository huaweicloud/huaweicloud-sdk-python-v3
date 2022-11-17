# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddProtectResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'commit': 'CommitRepoV2',
        'protected': 'bool',
        'developers_can_push': 'bool',
        'developers_can_merge': 'bool',
        'master_can_push': 'bool',
        'master_can_merge': 'bool',
        'no_one_can_push': 'bool',
        'no_one_can_merge': 'bool',
        'in_an_opened_merge_request': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'commit': 'commit',
        'protected': 'protected',
        'developers_can_push': 'developers_can_push',
        'developers_can_merge': 'developers_can_merge',
        'master_can_push': 'master_can_push',
        'master_can_merge': 'master_can_merge',
        'no_one_can_push': 'no_one_can_push',
        'no_one_can_merge': 'no_one_can_merge',
        'in_an_opened_merge_request': 'in_an_opened_merge_request'
    }

    def __init__(self, name=None, commit=None, protected=None, developers_can_push=None, developers_can_merge=None, master_can_push=None, master_can_merge=None, no_one_can_push=None, no_one_can_merge=None, in_an_opened_merge_request=None):
        """AddProtectResponse

        The model defined in huaweicloud sdk

        :param name: 分支名称
        :type name: str
        :param commit: 
        :type commit: :class:`huaweicloudsdkcodehub.v3.CommitRepoV2`
        :param protected: 是否保护
        :type protected: bool
        :param developers_can_push: 是否允许开发者提交
        :type developers_can_push: bool
        :param developers_can_merge: 是否允许开发者合并
        :type developers_can_merge: bool
        :param master_can_push: 是否允许管理员提交
        :type master_can_push: bool
        :param master_can_merge: 是否允许管理员合并
        :type master_can_merge: bool
        :param no_one_can_push: 没有人允许提交
        :type no_one_can_push: bool
        :param no_one_can_merge: 没有人允许合并
        :type no_one_can_merge: bool
        :param in_an_opened_merge_request: 是否在一个打开的合并请求
        :type in_an_opened_merge_request: bool
        """
        
        

        self._name = None
        self._commit = None
        self._protected = None
        self._developers_can_push = None
        self._developers_can_merge = None
        self._master_can_push = None
        self._master_can_merge = None
        self._no_one_can_push = None
        self._no_one_can_merge = None
        self._in_an_opened_merge_request = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if commit is not None:
            self.commit = commit
        if protected is not None:
            self.protected = protected
        if developers_can_push is not None:
            self.developers_can_push = developers_can_push
        if developers_can_merge is not None:
            self.developers_can_merge = developers_can_merge
        if master_can_push is not None:
            self.master_can_push = master_can_push
        if master_can_merge is not None:
            self.master_can_merge = master_can_merge
        if no_one_can_push is not None:
            self.no_one_can_push = no_one_can_push
        if no_one_can_merge is not None:
            self.no_one_can_merge = no_one_can_merge
        if in_an_opened_merge_request is not None:
            self.in_an_opened_merge_request = in_an_opened_merge_request

    @property
    def name(self):
        """Gets the name of this AddProtectResponse.

        分支名称

        :return: The name of this AddProtectResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddProtectResponse.

        分支名称

        :param name: The name of this AddProtectResponse.
        :type name: str
        """
        self._name = name

    @property
    def commit(self):
        """Gets the commit of this AddProtectResponse.

        :return: The commit of this AddProtectResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v3.CommitRepoV2`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this AddProtectResponse.

        :param commit: The commit of this AddProtectResponse.
        :type commit: :class:`huaweicloudsdkcodehub.v3.CommitRepoV2`
        """
        self._commit = commit

    @property
    def protected(self):
        """Gets the protected of this AddProtectResponse.

        是否保护

        :return: The protected of this AddProtectResponse.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this AddProtectResponse.

        是否保护

        :param protected: The protected of this AddProtectResponse.
        :type protected: bool
        """
        self._protected = protected

    @property
    def developers_can_push(self):
        """Gets the developers_can_push of this AddProtectResponse.

        是否允许开发者提交

        :return: The developers_can_push of this AddProtectResponse.
        :rtype: bool
        """
        return self._developers_can_push

    @developers_can_push.setter
    def developers_can_push(self, developers_can_push):
        """Sets the developers_can_push of this AddProtectResponse.

        是否允许开发者提交

        :param developers_can_push: The developers_can_push of this AddProtectResponse.
        :type developers_can_push: bool
        """
        self._developers_can_push = developers_can_push

    @property
    def developers_can_merge(self):
        """Gets the developers_can_merge of this AddProtectResponse.

        是否允许开发者合并

        :return: The developers_can_merge of this AddProtectResponse.
        :rtype: bool
        """
        return self._developers_can_merge

    @developers_can_merge.setter
    def developers_can_merge(self, developers_can_merge):
        """Sets the developers_can_merge of this AddProtectResponse.

        是否允许开发者合并

        :param developers_can_merge: The developers_can_merge of this AddProtectResponse.
        :type developers_can_merge: bool
        """
        self._developers_can_merge = developers_can_merge

    @property
    def master_can_push(self):
        """Gets the master_can_push of this AddProtectResponse.

        是否允许管理员提交

        :return: The master_can_push of this AddProtectResponse.
        :rtype: bool
        """
        return self._master_can_push

    @master_can_push.setter
    def master_can_push(self, master_can_push):
        """Sets the master_can_push of this AddProtectResponse.

        是否允许管理员提交

        :param master_can_push: The master_can_push of this AddProtectResponse.
        :type master_can_push: bool
        """
        self._master_can_push = master_can_push

    @property
    def master_can_merge(self):
        """Gets the master_can_merge of this AddProtectResponse.

        是否允许管理员合并

        :return: The master_can_merge of this AddProtectResponse.
        :rtype: bool
        """
        return self._master_can_merge

    @master_can_merge.setter
    def master_can_merge(self, master_can_merge):
        """Sets the master_can_merge of this AddProtectResponse.

        是否允许管理员合并

        :param master_can_merge: The master_can_merge of this AddProtectResponse.
        :type master_can_merge: bool
        """
        self._master_can_merge = master_can_merge

    @property
    def no_one_can_push(self):
        """Gets the no_one_can_push of this AddProtectResponse.

        没有人允许提交

        :return: The no_one_can_push of this AddProtectResponse.
        :rtype: bool
        """
        return self._no_one_can_push

    @no_one_can_push.setter
    def no_one_can_push(self, no_one_can_push):
        """Sets the no_one_can_push of this AddProtectResponse.

        没有人允许提交

        :param no_one_can_push: The no_one_can_push of this AddProtectResponse.
        :type no_one_can_push: bool
        """
        self._no_one_can_push = no_one_can_push

    @property
    def no_one_can_merge(self):
        """Gets the no_one_can_merge of this AddProtectResponse.

        没有人允许合并

        :return: The no_one_can_merge of this AddProtectResponse.
        :rtype: bool
        """
        return self._no_one_can_merge

    @no_one_can_merge.setter
    def no_one_can_merge(self, no_one_can_merge):
        """Sets the no_one_can_merge of this AddProtectResponse.

        没有人允许合并

        :param no_one_can_merge: The no_one_can_merge of this AddProtectResponse.
        :type no_one_can_merge: bool
        """
        self._no_one_can_merge = no_one_can_merge

    @property
    def in_an_opened_merge_request(self):
        """Gets the in_an_opened_merge_request of this AddProtectResponse.

        是否在一个打开的合并请求

        :return: The in_an_opened_merge_request of this AddProtectResponse.
        :rtype: bool
        """
        return self._in_an_opened_merge_request

    @in_an_opened_merge_request.setter
    def in_an_opened_merge_request(self, in_an_opened_merge_request):
        """Sets the in_an_opened_merge_request of this AddProtectResponse.

        是否在一个打开的合并请求

        :param in_an_opened_merge_request: The in_an_opened_merge_request of this AddProtectResponse.
        :type in_an_opened_merge_request: bool
        """
        self._in_an_opened_merge_request = in_an_opened_merge_request

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
        if not isinstance(other, AddProtectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

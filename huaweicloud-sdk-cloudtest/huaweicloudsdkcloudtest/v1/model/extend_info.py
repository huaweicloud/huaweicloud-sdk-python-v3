# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtendInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'author': 'ExtendAuthorInfo',
        'updator': 'ExtendAuthorInfo',
        'domain': 'AssignedUserInfo',
        'description': 'str',
        'preparation': 'str',
        'steps': 'list[ExternalServiceCaseStep]',
        'label_list': 'list[AssignedUserInfo]',
        'defect_list': 'list[AssignedUserInfo]',
        'module': 'AssignedUserInfo',
        'issue': 'AssignedUserInfo',
        'test_version_id': 'str',
        'fixed_version': 'AssignedUserInfo'
    }

    attribute_map = {
        'author': 'author',
        'updator': 'updator',
        'domain': 'domain',
        'description': 'description',
        'preparation': 'preparation',
        'steps': 'steps',
        'label_list': 'label_list',
        'defect_list': 'defect_list',
        'module': 'module',
        'issue': 'issue',
        'test_version_id': 'test_version_id',
        'fixed_version': 'fixed_version'
    }

    def __init__(self, author=None, updator=None, domain=None, description=None, preparation=None, steps=None, label_list=None, defect_list=None, module=None, issue=None, test_version_id=None, fixed_version=None):
        r"""ExtendInfo

        The model defined in huaweicloud sdk

        :param author: 
        :type author: :class:`huaweicloudsdkcloudtest.v1.ExtendAuthorInfo`
        :param updator: 
        :type updator: :class:`huaweicloudsdkcloudtest.v1.ExtendAuthorInfo`
        :param domain: 
        :type domain: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        :param description: 描述信息
        :type description: str
        :param preparation: 前置条件
        :type preparation: str
        :param steps: 测试步骤，数组长度小于10
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.ExternalServiceCaseStep`]
        :param label_list: 标签信息
        :type label_list: list[:class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`]
        :param defect_list: 缺陷信息
        :type defect_list: list[:class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`]
        :param module: 
        :type module: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        :param issue: 
        :type issue: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        :param test_version_id: 测试版本号
        :type test_version_id: str
        :param fixed_version: 
        :type fixed_version: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        
        

        self._author = None
        self._updator = None
        self._domain = None
        self._description = None
        self._preparation = None
        self._steps = None
        self._label_list = None
        self._defect_list = None
        self._module = None
        self._issue = None
        self._test_version_id = None
        self._fixed_version = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if updator is not None:
            self.updator = updator
        if domain is not None:
            self.domain = domain
        if description is not None:
            self.description = description
        if preparation is not None:
            self.preparation = preparation
        if steps is not None:
            self.steps = steps
        if label_list is not None:
            self.label_list = label_list
        if defect_list is not None:
            self.defect_list = defect_list
        if module is not None:
            self.module = module
        if issue is not None:
            self.issue = issue
        if test_version_id is not None:
            self.test_version_id = test_version_id
        if fixed_version is not None:
            self.fixed_version = fixed_version

    @property
    def author(self):
        r"""Gets the author of this ExtendInfo.

        :return: The author of this ExtendInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ExtendAuthorInfo`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this ExtendInfo.

        :param author: The author of this ExtendInfo.
        :type author: :class:`huaweicloudsdkcloudtest.v1.ExtendAuthorInfo`
        """
        self._author = author

    @property
    def updator(self):
        r"""Gets the updator of this ExtendInfo.

        :return: The updator of this ExtendInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ExtendAuthorInfo`
        """
        return self._updator

    @updator.setter
    def updator(self, updator):
        r"""Sets the updator of this ExtendInfo.

        :param updator: The updator of this ExtendInfo.
        :type updator: :class:`huaweicloudsdkcloudtest.v1.ExtendAuthorInfo`
        """
        self._updator = updator

    @property
    def domain(self):
        r"""Gets the domain of this ExtendInfo.

        :return: The domain of this ExtendInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ExtendInfo.

        :param domain: The domain of this ExtendInfo.
        :type domain: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        self._domain = domain

    @property
    def description(self):
        r"""Gets the description of this ExtendInfo.

        描述信息

        :return: The description of this ExtendInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExtendInfo.

        描述信息

        :param description: The description of this ExtendInfo.
        :type description: str
        """
        self._description = description

    @property
    def preparation(self):
        r"""Gets the preparation of this ExtendInfo.

        前置条件

        :return: The preparation of this ExtendInfo.
        :rtype: str
        """
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        r"""Sets the preparation of this ExtendInfo.

        前置条件

        :param preparation: The preparation of this ExtendInfo.
        :type preparation: str
        """
        self._preparation = preparation

    @property
    def steps(self):
        r"""Gets the steps of this ExtendInfo.

        测试步骤，数组长度小于10

        :return: The steps of this ExtendInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ExternalServiceCaseStep`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this ExtendInfo.

        测试步骤，数组长度小于10

        :param steps: The steps of this ExtendInfo.
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.ExternalServiceCaseStep`]
        """
        self._steps = steps

    @property
    def label_list(self):
        r"""Gets the label_list of this ExtendInfo.

        标签信息

        :return: The label_list of this ExtendInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this ExtendInfo.

        标签信息

        :param label_list: The label_list of this ExtendInfo.
        :type label_list: list[:class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`]
        """
        self._label_list = label_list

    @property
    def defect_list(self):
        r"""Gets the defect_list of this ExtendInfo.

        缺陷信息

        :return: The defect_list of this ExtendInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`]
        """
        return self._defect_list

    @defect_list.setter
    def defect_list(self, defect_list):
        r"""Sets the defect_list of this ExtendInfo.

        缺陷信息

        :param defect_list: The defect_list of this ExtendInfo.
        :type defect_list: list[:class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`]
        """
        self._defect_list = defect_list

    @property
    def module(self):
        r"""Gets the module of this ExtendInfo.

        :return: The module of this ExtendInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this ExtendInfo.

        :param module: The module of this ExtendInfo.
        :type module: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        self._module = module

    @property
    def issue(self):
        r"""Gets the issue of this ExtendInfo.

        :return: The issue of this ExtendInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        r"""Sets the issue of this ExtendInfo.

        :param issue: The issue of this ExtendInfo.
        :type issue: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        self._issue = issue

    @property
    def test_version_id(self):
        r"""Gets the test_version_id of this ExtendInfo.

        测试版本号

        :return: The test_version_id of this ExtendInfo.
        :rtype: str
        """
        return self._test_version_id

    @test_version_id.setter
    def test_version_id(self, test_version_id):
        r"""Sets the test_version_id of this ExtendInfo.

        测试版本号

        :param test_version_id: The test_version_id of this ExtendInfo.
        :type test_version_id: str
        """
        self._test_version_id = test_version_id

    @property
    def fixed_version(self):
        r"""Gets the fixed_version of this ExtendInfo.

        :return: The fixed_version of this ExtendInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        return self._fixed_version

    @fixed_version.setter
    def fixed_version(self, fixed_version):
        r"""Sets the fixed_version of this ExtendInfo.

        :param fixed_version: The fixed_version of this ExtendInfo.
        :type fixed_version: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        self._fixed_version = fixed_version

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
        if not isinstance(other, ExtendInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

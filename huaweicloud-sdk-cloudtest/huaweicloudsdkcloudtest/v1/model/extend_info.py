# coding: utf-8

import pprint
import re

import six





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
        """ExtendInfo - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the author of this ExtendInfo.


        :return: The author of this ExtendInfo.
        :rtype: ExtendAuthorInfo
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ExtendInfo.


        :param author: The author of this ExtendInfo.
        :type: ExtendAuthorInfo
        """
        self._author = author

    @property
    def updator(self):
        """Gets the updator of this ExtendInfo.


        :return: The updator of this ExtendInfo.
        :rtype: ExtendAuthorInfo
        """
        return self._updator

    @updator.setter
    def updator(self, updator):
        """Sets the updator of this ExtendInfo.


        :param updator: The updator of this ExtendInfo.
        :type: ExtendAuthorInfo
        """
        self._updator = updator

    @property
    def domain(self):
        """Gets the domain of this ExtendInfo.


        :return: The domain of this ExtendInfo.
        :rtype: AssignedUserInfo
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ExtendInfo.


        :param domain: The domain of this ExtendInfo.
        :type: AssignedUserInfo
        """
        self._domain = domain

    @property
    def description(self):
        """Gets the description of this ExtendInfo.

        描述信息

        :return: The description of this ExtendInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExtendInfo.

        描述信息

        :param description: The description of this ExtendInfo.
        :type: str
        """
        self._description = description

    @property
    def preparation(self):
        """Gets the preparation of this ExtendInfo.

        前置条件

        :return: The preparation of this ExtendInfo.
        :rtype: str
        """
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        """Sets the preparation of this ExtendInfo.

        前置条件

        :param preparation: The preparation of this ExtendInfo.
        :type: str
        """
        self._preparation = preparation

    @property
    def steps(self):
        """Gets the steps of this ExtendInfo.

        测试步骤，数组长度小于10

        :return: The steps of this ExtendInfo.
        :rtype: list[ExternalServiceCaseStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this ExtendInfo.

        测试步骤，数组长度小于10

        :param steps: The steps of this ExtendInfo.
        :type: list[ExternalServiceCaseStep]
        """
        self._steps = steps

    @property
    def label_list(self):
        """Gets the label_list of this ExtendInfo.

        标签信息

        :return: The label_list of this ExtendInfo.
        :rtype: list[AssignedUserInfo]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        """Sets the label_list of this ExtendInfo.

        标签信息

        :param label_list: The label_list of this ExtendInfo.
        :type: list[AssignedUserInfo]
        """
        self._label_list = label_list

    @property
    def defect_list(self):
        """Gets the defect_list of this ExtendInfo.

        缺陷信息

        :return: The defect_list of this ExtendInfo.
        :rtype: list[AssignedUserInfo]
        """
        return self._defect_list

    @defect_list.setter
    def defect_list(self, defect_list):
        """Sets the defect_list of this ExtendInfo.

        缺陷信息

        :param defect_list: The defect_list of this ExtendInfo.
        :type: list[AssignedUserInfo]
        """
        self._defect_list = defect_list

    @property
    def module(self):
        """Gets the module of this ExtendInfo.


        :return: The module of this ExtendInfo.
        :rtype: AssignedUserInfo
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this ExtendInfo.


        :param module: The module of this ExtendInfo.
        :type: AssignedUserInfo
        """
        self._module = module

    @property
    def issue(self):
        """Gets the issue of this ExtendInfo.


        :return: The issue of this ExtendInfo.
        :rtype: AssignedUserInfo
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """Sets the issue of this ExtendInfo.


        :param issue: The issue of this ExtendInfo.
        :type: AssignedUserInfo
        """
        self._issue = issue

    @property
    def test_version_id(self):
        """Gets the test_version_id of this ExtendInfo.

        测试版本号

        :return: The test_version_id of this ExtendInfo.
        :rtype: str
        """
        return self._test_version_id

    @test_version_id.setter
    def test_version_id(self, test_version_id):
        """Sets the test_version_id of this ExtendInfo.

        测试版本号

        :param test_version_id: The test_version_id of this ExtendInfo.
        :type: str
        """
        self._test_version_id = test_version_id

    @property
    def fixed_version(self):
        """Gets the fixed_version of this ExtendInfo.


        :return: The fixed_version of this ExtendInfo.
        :rtype: AssignedUserInfo
        """
        return self._fixed_version

    @fixed_version.setter
    def fixed_version(self, fixed_version):
        """Sets the fixed_version of this ExtendInfo.


        :param fixed_version: The fixed_version of this ExtendInfo.
        :type: AssignedUserInfo
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExtendInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

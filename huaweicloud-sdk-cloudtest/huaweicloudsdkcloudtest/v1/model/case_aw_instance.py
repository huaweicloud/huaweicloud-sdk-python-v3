# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseAwInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'setup_aw_list': 'list[AwInstance]',
        'teardown_aw_list': 'list[AwInstance]',
        'test_aw_list': 'list[AwInstance]'
    }

    attribute_map = {
        'setup_aw_list': 'setup_aw_list',
        'teardown_aw_list': 'teardown_aw_list',
        'test_aw_list': 'test_aw_list'
    }

    def __init__(self, setup_aw_list=None, teardown_aw_list=None, test_aw_list=None):
        r"""CaseAwInstance

        The model defined in huaweicloud sdk

        :param setup_aw_list: 测试用例前置步骤
        :type setup_aw_list: list[:class:`huaweicloudsdkcloudtest.v1.AwInstance`]
        :param teardown_aw_list: 测试步骤
        :type teardown_aw_list: list[:class:`huaweicloudsdkcloudtest.v1.AwInstance`]
        :param test_aw_list: 测试用例后置不走
        :type test_aw_list: list[:class:`huaweicloudsdkcloudtest.v1.AwInstance`]
        """
        
        

        self._setup_aw_list = None
        self._teardown_aw_list = None
        self._test_aw_list = None
        self.discriminator = None

        if setup_aw_list is not None:
            self.setup_aw_list = setup_aw_list
        if teardown_aw_list is not None:
            self.teardown_aw_list = teardown_aw_list
        if test_aw_list is not None:
            self.test_aw_list = test_aw_list

    @property
    def setup_aw_list(self):
        r"""Gets the setup_aw_list of this CaseAwInstance.

        测试用例前置步骤

        :return: The setup_aw_list of this CaseAwInstance.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwInstance`]
        """
        return self._setup_aw_list

    @setup_aw_list.setter
    def setup_aw_list(self, setup_aw_list):
        r"""Sets the setup_aw_list of this CaseAwInstance.

        测试用例前置步骤

        :param setup_aw_list: The setup_aw_list of this CaseAwInstance.
        :type setup_aw_list: list[:class:`huaweicloudsdkcloudtest.v1.AwInstance`]
        """
        self._setup_aw_list = setup_aw_list

    @property
    def teardown_aw_list(self):
        r"""Gets the teardown_aw_list of this CaseAwInstance.

        测试步骤

        :return: The teardown_aw_list of this CaseAwInstance.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwInstance`]
        """
        return self._teardown_aw_list

    @teardown_aw_list.setter
    def teardown_aw_list(self, teardown_aw_list):
        r"""Sets the teardown_aw_list of this CaseAwInstance.

        测试步骤

        :param teardown_aw_list: The teardown_aw_list of this CaseAwInstance.
        :type teardown_aw_list: list[:class:`huaweicloudsdkcloudtest.v1.AwInstance`]
        """
        self._teardown_aw_list = teardown_aw_list

    @property
    def test_aw_list(self):
        r"""Gets the test_aw_list of this CaseAwInstance.

        测试用例后置不走

        :return: The test_aw_list of this CaseAwInstance.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwInstance`]
        """
        return self._test_aw_list

    @test_aw_list.setter
    def test_aw_list(self, test_aw_list):
        r"""Sets the test_aw_list of this CaseAwInstance.

        测试用例后置不走

        :param test_aw_list: The test_aw_list of this CaseAwInstance.
        :type test_aw_list: list[:class:`huaweicloudsdkcloudtest.v1.AwInstance`]
        """
        self._test_aw_list = test_aw_list

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
        if not isinstance(other, CaseAwInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

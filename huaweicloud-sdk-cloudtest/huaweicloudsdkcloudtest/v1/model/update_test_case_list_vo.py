# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTestCaseListVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'success_list': 'list[str]',
        'failed_list': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'success_list': 'success_list',
        'failed_list': 'failed_list'
    }

    def __init__(self, id=None, name=None, success_list=None, failed_list=None):
        r"""UpdateTestCaseListVo

        The model defined in huaweicloud sdk

        :param id: CTS需要返回资源id
        :type id: str
        :param name: CTS需要返回资源name
        :type name: str
        :param success_list: 成功批量更新用例的id列表
        :type success_list: list[str]
        :param failed_list: 没有批量更新用例的id列表
        :type failed_list: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._success_list = None
        self._failed_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if success_list is not None:
            self.success_list = success_list
        if failed_list is not None:
            self.failed_list = failed_list

    @property
    def id(self):
        r"""Gets the id of this UpdateTestCaseListVo.

        CTS需要返回资源id

        :return: The id of this UpdateTestCaseListVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateTestCaseListVo.

        CTS需要返回资源id

        :param id: The id of this UpdateTestCaseListVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateTestCaseListVo.

        CTS需要返回资源name

        :return: The name of this UpdateTestCaseListVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateTestCaseListVo.

        CTS需要返回资源name

        :param name: The name of this UpdateTestCaseListVo.
        :type name: str
        """
        self._name = name

    @property
    def success_list(self):
        r"""Gets the success_list of this UpdateTestCaseListVo.

        成功批量更新用例的id列表

        :return: The success_list of this UpdateTestCaseListVo.
        :rtype: list[str]
        """
        return self._success_list

    @success_list.setter
    def success_list(self, success_list):
        r"""Sets the success_list of this UpdateTestCaseListVo.

        成功批量更新用例的id列表

        :param success_list: The success_list of this UpdateTestCaseListVo.
        :type success_list: list[str]
        """
        self._success_list = success_list

    @property
    def failed_list(self):
        r"""Gets the failed_list of this UpdateTestCaseListVo.

        没有批量更新用例的id列表

        :return: The failed_list of this UpdateTestCaseListVo.
        :rtype: list[str]
        """
        return self._failed_list

    @failed_list.setter
    def failed_list(self, failed_list):
        r"""Sets the failed_list of this UpdateTestCaseListVo.

        没有批量更新用例的id列表

        :param failed_list: The failed_list of this UpdateTestCaseListVo.
        :type failed_list: list[str]
        """
        self._failed_list = failed_list

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
        if not isinstance(other, UpdateTestCaseListVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

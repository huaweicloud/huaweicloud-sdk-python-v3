# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowActionIInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'build_no': 'int',
        'start_offset': 'int',
        'end_offset': 'int',
        'sort': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'build_no': 'build_no',
        'start_offset': 'start_offset',
        'end_offset': 'end_offset',
        'sort': 'sort'
    }

    def __init__(self, job_id=None, build_no=None, start_offset=None, end_offset=None, sort=None):
        r"""ShowActionIInfoRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param build_no: 构建任务的构建编号，从1开始，每次构建递增1
        :type build_no: int
        :param start_offset: **参数解释**： 起始偏移量，表示从此开始查询。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，大于等于0。
        :type start_offset: int
        :param end_offset: **参数解释**： 结束偏移量，表示查询到此结束。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，大于等于0。
        :type end_offset: int
        :param sort: **参数解释**： 排序方式。 **约束限制**： 不涉及。 **取值范围**： AES|DESC。
        :type sort: str
        """
        
        

        self._job_id = None
        self._build_no = None
        self._start_offset = None
        self._end_offset = None
        self._sort = None
        self.discriminator = None

        self.job_id = job_id
        self.build_no = build_no
        self.start_offset = start_offset
        self.end_offset = end_offset
        if sort is not None:
            self.sort = sort

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowActionIInfoRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this ShowActionIInfoRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowActionIInfoRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this ShowActionIInfoRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def build_no(self):
        r"""Gets the build_no of this ShowActionIInfoRequest.

        构建任务的构建编号，从1开始，每次构建递增1

        :return: The build_no of this ShowActionIInfoRequest.
        :rtype: int
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this ShowActionIInfoRequest.

        构建任务的构建编号，从1开始，每次构建递增1

        :param build_no: The build_no of this ShowActionIInfoRequest.
        :type build_no: int
        """
        self._build_no = build_no

    @property
    def start_offset(self):
        r"""Gets the start_offset of this ShowActionIInfoRequest.

        **参数解释**： 起始偏移量，表示从此开始查询。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，大于等于0。

        :return: The start_offset of this ShowActionIInfoRequest.
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        r"""Sets the start_offset of this ShowActionIInfoRequest.

        **参数解释**： 起始偏移量，表示从此开始查询。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，大于等于0。

        :param start_offset: The start_offset of this ShowActionIInfoRequest.
        :type start_offset: int
        """
        self._start_offset = start_offset

    @property
    def end_offset(self):
        r"""Gets the end_offset of this ShowActionIInfoRequest.

        **参数解释**： 结束偏移量，表示查询到此结束。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，大于等于0。

        :return: The end_offset of this ShowActionIInfoRequest.
        :rtype: int
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        r"""Sets the end_offset of this ShowActionIInfoRequest.

        **参数解释**： 结束偏移量，表示查询到此结束。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，大于等于0。

        :param end_offset: The end_offset of this ShowActionIInfoRequest.
        :type end_offset: int
        """
        self._end_offset = end_offset

    @property
    def sort(self):
        r"""Gets the sort of this ShowActionIInfoRequest.

        **参数解释**： 排序方式。 **约束限制**： 不涉及。 **取值范围**： AES|DESC。

        :return: The sort of this ShowActionIInfoRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ShowActionIInfoRequest.

        **参数解释**： 排序方式。 **约束限制**： 不涉及。 **取值范围**： AES|DESC。

        :param sort: The sort of this ShowActionIInfoRequest.
        :type sort: str
        """
        self._sort = sort

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
        if not isinstance(other, ShowActionIInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

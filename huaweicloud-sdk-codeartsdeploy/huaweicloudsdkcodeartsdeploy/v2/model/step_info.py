# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StepInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'id': 'int',
        'offset': 'int',
        'enable': 'bool',
        'name': 'str',
        'current_offset': 'int',
        'elapsed_time': 'int',
        'faq_url': 'str'
    }

    attribute_map = {
        'region': 'region',
        'id': 'id',
        'offset': 'offset',
        'enable': 'enable',
        'name': 'name',
        'current_offset': 'current_offset',
        'elapsed_time': 'elapsed_time',
        'faq_url': 'faq_url'
    }

    def __init__(self, region=None, id=None, offset=None, enable=None, name=None, current_offset=None, elapsed_time=None, faq_url=None):
        r"""StepInfo

        The model defined in huaweicloud sdk

        :param region: 请求的region
        :type region: str
        :param id: 应用id
        :type id: int
        :param offset: 偏移量
        :type offset: int
        :param enable: 是否启用
        :type enable: bool
        :param name: 步骤名称
        :type name: str
        :param current_offset: 当前偏移量
        :type current_offset: int
        :param elapsed_time: 任务执行时长
        :type elapsed_time: int
        :param faq_url: 常见问题
        :type faq_url: str
        """
        
        

        self._region = None
        self._id = None
        self._offset = None
        self._enable = None
        self._name = None
        self._current_offset = None
        self._elapsed_time = None
        self._faq_url = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if id is not None:
            self.id = id
        if offset is not None:
            self.offset = offset
        if enable is not None:
            self.enable = enable
        if name is not None:
            self.name = name
        if current_offset is not None:
            self.current_offset = current_offset
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if faq_url is not None:
            self.faq_url = faq_url

    @property
    def region(self):
        r"""Gets the region of this StepInfo.

        请求的region

        :return: The region of this StepInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this StepInfo.

        请求的region

        :param region: The region of this StepInfo.
        :type region: str
        """
        self._region = region

    @property
    def id(self):
        r"""Gets the id of this StepInfo.

        应用id

        :return: The id of this StepInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StepInfo.

        应用id

        :param id: The id of this StepInfo.
        :type id: int
        """
        self._id = id

    @property
    def offset(self):
        r"""Gets the offset of this StepInfo.

        偏移量

        :return: The offset of this StepInfo.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this StepInfo.

        偏移量

        :param offset: The offset of this StepInfo.
        :type offset: int
        """
        self._offset = offset

    @property
    def enable(self):
        r"""Gets the enable of this StepInfo.

        是否启用

        :return: The enable of this StepInfo.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this StepInfo.

        是否启用

        :param enable: The enable of this StepInfo.
        :type enable: bool
        """
        self._enable = enable

    @property
    def name(self):
        r"""Gets the name of this StepInfo.

        步骤名称

        :return: The name of this StepInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StepInfo.

        步骤名称

        :param name: The name of this StepInfo.
        :type name: str
        """
        self._name = name

    @property
    def current_offset(self):
        r"""Gets the current_offset of this StepInfo.

        当前偏移量

        :return: The current_offset of this StepInfo.
        :rtype: int
        """
        return self._current_offset

    @current_offset.setter
    def current_offset(self, current_offset):
        r"""Sets the current_offset of this StepInfo.

        当前偏移量

        :param current_offset: The current_offset of this StepInfo.
        :type current_offset: int
        """
        self._current_offset = current_offset

    @property
    def elapsed_time(self):
        r"""Gets the elapsed_time of this StepInfo.

        任务执行时长

        :return: The elapsed_time of this StepInfo.
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        r"""Sets the elapsed_time of this StepInfo.

        任务执行时长

        :param elapsed_time: The elapsed_time of this StepInfo.
        :type elapsed_time: int
        """
        self._elapsed_time = elapsed_time

    @property
    def faq_url(self):
        r"""Gets the faq_url of this StepInfo.

        常见问题

        :return: The faq_url of this StepInfo.
        :rtype: str
        """
        return self._faq_url

    @faq_url.setter
    def faq_url(self, faq_url):
        r"""Sets the faq_url of this StepInfo.

        常见问题

        :param faq_url: The faq_url of this StepInfo.
        :type faq_url: str
        """
        self._faq_url = faq_url

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
        if not isinstance(other, StepInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

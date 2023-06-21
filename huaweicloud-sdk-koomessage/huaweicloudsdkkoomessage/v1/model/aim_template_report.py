# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIMTemplateReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tpl_id': 'str',
        'start_time': 'str',
        'resolving_times': 'int',
        'end_time': 'str',
        'expose_uv': 'int',
        'expose_pv': 'int',
        'click_uv': 'int',
        'click_pv': 'int'
    }

    attribute_map = {
        'tpl_id': 'tpl_id',
        'start_time': 'start_time',
        'resolving_times': 'resolving_times',
        'end_time': 'end_time',
        'expose_uv': 'expose_uv',
        'expose_pv': 'expose_pv',
        'click_uv': 'click_uv',
        'click_pv': 'click_pv'
    }

    def __init__(self, tpl_id=None, start_time=None, resolving_times=None, end_time=None, expose_uv=None, expose_pv=None, click_uv=None, click_pv=None):
        """AIMTemplateReport

        The model defined in huaweicloud sdk

        :param tpl_id: 智能信息模板ID。
        :type tpl_id: str
        :param start_time: 统计开始时间。样例为：1970-01-01T00:00:00Z。
        :type start_time: str
        :param resolving_times: 实际已解析数。
        :type resolving_times: int
        :param end_time: 统计结束时间。样例为：1970-01-01T00:00:00Z。
        :type end_time: str
        :param expose_uv: 消息曝光数。 
        :type expose_uv: int
        :param expose_pv: 消息曝光次数。 
        :type expose_pv: int
        :param click_uv: 消息点击数。 
        :type click_uv: int
        :param click_pv: 消息点击次数。 
        :type click_pv: int
        """
        
        

        self._tpl_id = None
        self._start_time = None
        self._resolving_times = None
        self._end_time = None
        self._expose_uv = None
        self._expose_pv = None
        self._click_uv = None
        self._click_pv = None
        self.discriminator = None

        if tpl_id is not None:
            self.tpl_id = tpl_id
        if start_time is not None:
            self.start_time = start_time
        if resolving_times is not None:
            self.resolving_times = resolving_times
        if end_time is not None:
            self.end_time = end_time
        if expose_uv is not None:
            self.expose_uv = expose_uv
        if expose_pv is not None:
            self.expose_pv = expose_pv
        if click_uv is not None:
            self.click_uv = click_uv
        if click_pv is not None:
            self.click_pv = click_pv

    @property
    def tpl_id(self):
        """Gets the tpl_id of this AIMTemplateReport.

        智能信息模板ID。

        :return: The tpl_id of this AIMTemplateReport.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this AIMTemplateReport.

        智能信息模板ID。

        :param tpl_id: The tpl_id of this AIMTemplateReport.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def start_time(self):
        """Gets the start_time of this AIMTemplateReport.

        统计开始时间。样例为：1970-01-01T00:00:00Z。

        :return: The start_time of this AIMTemplateReport.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AIMTemplateReport.

        统计开始时间。样例为：1970-01-01T00:00:00Z。

        :param start_time: The start_time of this AIMTemplateReport.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def resolving_times(self):
        """Gets the resolving_times of this AIMTemplateReport.

        实际已解析数。

        :return: The resolving_times of this AIMTemplateReport.
        :rtype: int
        """
        return self._resolving_times

    @resolving_times.setter
    def resolving_times(self, resolving_times):
        """Sets the resolving_times of this AIMTemplateReport.

        实际已解析数。

        :param resolving_times: The resolving_times of this AIMTemplateReport.
        :type resolving_times: int
        """
        self._resolving_times = resolving_times

    @property
    def end_time(self):
        """Gets the end_time of this AIMTemplateReport.

        统计结束时间。样例为：1970-01-01T00:00:00Z。

        :return: The end_time of this AIMTemplateReport.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AIMTemplateReport.

        统计结束时间。样例为：1970-01-01T00:00:00Z。

        :param end_time: The end_time of this AIMTemplateReport.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def expose_uv(self):
        """Gets the expose_uv of this AIMTemplateReport.

        消息曝光数。 

        :return: The expose_uv of this AIMTemplateReport.
        :rtype: int
        """
        return self._expose_uv

    @expose_uv.setter
    def expose_uv(self, expose_uv):
        """Sets the expose_uv of this AIMTemplateReport.

        消息曝光数。 

        :param expose_uv: The expose_uv of this AIMTemplateReport.
        :type expose_uv: int
        """
        self._expose_uv = expose_uv

    @property
    def expose_pv(self):
        """Gets the expose_pv of this AIMTemplateReport.

        消息曝光次数。 

        :return: The expose_pv of this AIMTemplateReport.
        :rtype: int
        """
        return self._expose_pv

    @expose_pv.setter
    def expose_pv(self, expose_pv):
        """Sets the expose_pv of this AIMTemplateReport.

        消息曝光次数。 

        :param expose_pv: The expose_pv of this AIMTemplateReport.
        :type expose_pv: int
        """
        self._expose_pv = expose_pv

    @property
    def click_uv(self):
        """Gets the click_uv of this AIMTemplateReport.

        消息点击数。 

        :return: The click_uv of this AIMTemplateReport.
        :rtype: int
        """
        return self._click_uv

    @click_uv.setter
    def click_uv(self, click_uv):
        """Sets the click_uv of this AIMTemplateReport.

        消息点击数。 

        :param click_uv: The click_uv of this AIMTemplateReport.
        :type click_uv: int
        """
        self._click_uv = click_uv

    @property
    def click_pv(self):
        """Gets the click_pv of this AIMTemplateReport.

        消息点击次数。 

        :return: The click_pv of this AIMTemplateReport.
        :rtype: int
        """
        return self._click_pv

    @click_pv.setter
    def click_pv(self, click_pv):
        """Sets the click_pv of this AIMTemplateReport.

        消息点击次数。 

        :param click_pv: The click_pv of this AIMTemplateReport.
        :type click_pv: int
        """
        self._click_pv = click_pv

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
        if not isinstance(other, AIMTemplateReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

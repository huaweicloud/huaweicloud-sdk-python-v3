# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'brokens': 'ReportbrokensInfo',
        'details': 'ReportdetailsInfo',
        'outline': 'ReportoutlineInfo',
        'rtproportion': 'str',
        'task_info': 'ReportTaskInfo',
        'resp_time_range': 'object'
    }

    attribute_map = {
        'brokens': 'brokens',
        'details': 'details',
        'outline': 'outline',
        'rtproportion': 'rtproportion',
        'task_info': 'taskInfo',
        'resp_time_range': 'respTimeRange'
    }

    def __init__(self, brokens=None, details=None, outline=None, rtproportion=None, task_info=None, resp_time_range=None):
        """ReportInfo

        The model defined in huaweicloud sdk

        :param brokens: 
        :type brokens: :class:`huaweicloudsdkcpts.v1.ReportbrokensInfo`
        :param details: 
        :type details: :class:`huaweicloudsdkcpts.v1.ReportdetailsInfo`
        :param outline: 
        :type outline: :class:`huaweicloudsdkcpts.v1.ReportoutlineInfo`
        :param rtproportion: 响应时间分布
        :type rtproportion: str
        :param task_info: 
        :type task_info: :class:`huaweicloudsdkcpts.v1.ReportTaskInfo`
        :param resp_time_range: 响应时间分布
        :type resp_time_range: object
        """
        
        

        self._brokens = None
        self._details = None
        self._outline = None
        self._rtproportion = None
        self._task_info = None
        self._resp_time_range = None
        self.discriminator = None

        if brokens is not None:
            self.brokens = brokens
        if details is not None:
            self.details = details
        if outline is not None:
            self.outline = outline
        if rtproportion is not None:
            self.rtproportion = rtproportion
        if task_info is not None:
            self.task_info = task_info
        if resp_time_range is not None:
            self.resp_time_range = resp_time_range

    @property
    def brokens(self):
        """Gets the brokens of this ReportInfo.


        :return: The brokens of this ReportInfo.
        :rtype: :class:`huaweicloudsdkcpts.v1.ReportbrokensInfo`
        """
        return self._brokens

    @brokens.setter
    def brokens(self, brokens):
        """Sets the brokens of this ReportInfo.


        :param brokens: The brokens of this ReportInfo.
        :type brokens: :class:`huaweicloudsdkcpts.v1.ReportbrokensInfo`
        """
        self._brokens = brokens

    @property
    def details(self):
        """Gets the details of this ReportInfo.


        :return: The details of this ReportInfo.
        :rtype: :class:`huaweicloudsdkcpts.v1.ReportdetailsInfo`
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ReportInfo.


        :param details: The details of this ReportInfo.
        :type details: :class:`huaweicloudsdkcpts.v1.ReportdetailsInfo`
        """
        self._details = details

    @property
    def outline(self):
        """Gets the outline of this ReportInfo.


        :return: The outline of this ReportInfo.
        :rtype: :class:`huaweicloudsdkcpts.v1.ReportoutlineInfo`
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this ReportInfo.


        :param outline: The outline of this ReportInfo.
        :type outline: :class:`huaweicloudsdkcpts.v1.ReportoutlineInfo`
        """
        self._outline = outline

    @property
    def rtproportion(self):
        """Gets the rtproportion of this ReportInfo.

        响应时间分布

        :return: The rtproportion of this ReportInfo.
        :rtype: str
        """
        return self._rtproportion

    @rtproportion.setter
    def rtproportion(self, rtproportion):
        """Sets the rtproportion of this ReportInfo.

        响应时间分布

        :param rtproportion: The rtproportion of this ReportInfo.
        :type rtproportion: str
        """
        self._rtproportion = rtproportion

    @property
    def task_info(self):
        """Gets the task_info of this ReportInfo.


        :return: The task_info of this ReportInfo.
        :rtype: :class:`huaweicloudsdkcpts.v1.ReportTaskInfo`
        """
        return self._task_info

    @task_info.setter
    def task_info(self, task_info):
        """Sets the task_info of this ReportInfo.


        :param task_info: The task_info of this ReportInfo.
        :type task_info: :class:`huaweicloudsdkcpts.v1.ReportTaskInfo`
        """
        self._task_info = task_info

    @property
    def resp_time_range(self):
        """Gets the resp_time_range of this ReportInfo.

        响应时间分布

        :return: The resp_time_range of this ReportInfo.
        :rtype: object
        """
        return self._resp_time_range

    @resp_time_range.setter
    def resp_time_range(self, resp_time_range):
        """Sets the resp_time_range of this ReportInfo.

        响应时间分布

        :param resp_time_range: The resp_time_range of this ReportInfo.
        :type resp_time_range: object
        """
        self._resp_time_range = resp_time_range

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
        if not isinstance(other, ReportInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

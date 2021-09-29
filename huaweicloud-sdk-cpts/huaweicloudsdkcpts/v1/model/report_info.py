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
        'task_info': 'ReportTaskInfo'
    }

    attribute_map = {
        'brokens': 'brokens',
        'details': 'details',
        'outline': 'outline',
        'rtproportion': 'rtproportion',
        'task_info': 'taskInfo'
    }

    def __init__(self, brokens=None, details=None, outline=None, rtproportion=None, task_info=None):
        """ReportInfo - a model defined in huaweicloud sdk"""
        
        

        self._brokens = None
        self._details = None
        self._outline = None
        self._rtproportion = None
        self._task_info = None
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

    @property
    def brokens(self):
        """Gets the brokens of this ReportInfo.


        :return: The brokens of this ReportInfo.
        :rtype: ReportbrokensInfo
        """
        return self._brokens

    @brokens.setter
    def brokens(self, brokens):
        """Sets the brokens of this ReportInfo.


        :param brokens: The brokens of this ReportInfo.
        :type: ReportbrokensInfo
        """
        self._brokens = brokens

    @property
    def details(self):
        """Gets the details of this ReportInfo.


        :return: The details of this ReportInfo.
        :rtype: ReportdetailsInfo
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ReportInfo.


        :param details: The details of this ReportInfo.
        :type: ReportdetailsInfo
        """
        self._details = details

    @property
    def outline(self):
        """Gets the outline of this ReportInfo.


        :return: The outline of this ReportInfo.
        :rtype: ReportoutlineInfo
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this ReportInfo.


        :param outline: The outline of this ReportInfo.
        :type: ReportoutlineInfo
        """
        self._outline = outline

    @property
    def rtproportion(self):
        """Gets the rtproportion of this ReportInfo.

        rtproportion

        :return: The rtproportion of this ReportInfo.
        :rtype: str
        """
        return self._rtproportion

    @rtproportion.setter
    def rtproportion(self, rtproportion):
        """Sets the rtproportion of this ReportInfo.

        rtproportion

        :param rtproportion: The rtproportion of this ReportInfo.
        :type: str
        """
        self._rtproportion = rtproportion

    @property
    def task_info(self):
        """Gets the task_info of this ReportInfo.


        :return: The task_info of this ReportInfo.
        :rtype: ReportTaskInfo
        """
        return self._task_info

    @task_info.setter
    def task_info(self, task_info):
        """Sets the task_info of this ReportInfo.


        :param task_info: The task_info of this ReportInfo.
        :type: ReportTaskInfo
        """
        self._task_info = task_info

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

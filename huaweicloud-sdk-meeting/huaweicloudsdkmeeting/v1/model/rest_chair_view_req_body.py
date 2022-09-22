# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestChairViewReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'view_type': 'int',
        'participant_id': 'str',
        'switch_time': 'int',
        'status': 'int'
    }

    attribute_map = {
        'view_type': 'viewType',
        'participant_id': 'participantID',
        'switch_time': 'switchTime',
        'status': 'status'
    }

    def __init__(self, view_type=None, participant_id=None, switch_time=None, status=None):
        """RestChairViewReqBody

        The model defined in huaweicloud sdk

        :param view_type: 主持人观看的画面类型。 - 0: 主持人轮询 - 1: 主持人观看多画面 - 2: 主持人选看会场
        :type view_type: int
        :param participant_id: 被主持人选看的会场。 当为主持人选看会场时为必填参数。
        :type participant_id: str
        :param switch_time: 轮询间隔，单位：秒。 主持人轮询时，必填字段。 范围:[10-120]，默认值：10。
        :type switch_time: int
        :param status: 启动/停止轮询。 主持人轮询时，必填字段。 - 0: 停止轮询 - 1: 启动轮询
        :type status: int
        """
        
        

        self._view_type = None
        self._participant_id = None
        self._switch_time = None
        self._status = None
        self.discriminator = None

        self.view_type = view_type
        if participant_id is not None:
            self.participant_id = participant_id
        if switch_time is not None:
            self.switch_time = switch_time
        if status is not None:
            self.status = status

    @property
    def view_type(self):
        """Gets the view_type of this RestChairViewReqBody.

        主持人观看的画面类型。 - 0: 主持人轮询 - 1: 主持人观看多画面 - 2: 主持人选看会场

        :return: The view_type of this RestChairViewReqBody.
        :rtype: int
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """Sets the view_type of this RestChairViewReqBody.

        主持人观看的画面类型。 - 0: 主持人轮询 - 1: 主持人观看多画面 - 2: 主持人选看会场

        :param view_type: The view_type of this RestChairViewReqBody.
        :type view_type: int
        """
        self._view_type = view_type

    @property
    def participant_id(self):
        """Gets the participant_id of this RestChairViewReqBody.

        被主持人选看的会场。 当为主持人选看会场时为必填参数。

        :return: The participant_id of this RestChairViewReqBody.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this RestChairViewReqBody.

        被主持人选看的会场。 当为主持人选看会场时为必填参数。

        :param participant_id: The participant_id of this RestChairViewReqBody.
        :type participant_id: str
        """
        self._participant_id = participant_id

    @property
    def switch_time(self):
        """Gets the switch_time of this RestChairViewReqBody.

        轮询间隔，单位：秒。 主持人轮询时，必填字段。 范围:[10-120]，默认值：10。

        :return: The switch_time of this RestChairViewReqBody.
        :rtype: int
        """
        return self._switch_time

    @switch_time.setter
    def switch_time(self, switch_time):
        """Sets the switch_time of this RestChairViewReqBody.

        轮询间隔，单位：秒。 主持人轮询时，必填字段。 范围:[10-120]，默认值：10。

        :param switch_time: The switch_time of this RestChairViewReqBody.
        :type switch_time: int
        """
        self._switch_time = switch_time

    @property
    def status(self):
        """Gets the status of this RestChairViewReqBody.

        启动/停止轮询。 主持人轮询时，必填字段。 - 0: 停止轮询 - 1: 启动轮询

        :return: The status of this RestChairViewReqBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RestChairViewReqBody.

        启动/停止轮询。 主持人轮询时，必填字段。 - 0: 停止轮询 - 1: 启动轮询

        :param status: The status of this RestChairViewReqBody.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, RestChairViewReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'body': 'RecordControlInfo'
    }

    attribute_map = {
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, action=None, body=None):
        """RunRecordRequest

        The model defined in huaweicloud sdk

        :param action: 操作行为。 取值如下： - START：对指定流开始录制，必须在直播流已经推送情况下才能正常启动，使用此命令启动录制的直播流如果发生了断流且超出断流时长，就会停止录制，并且重新推流后不会自动启动录制。 - STOP：对指定流停止录制。 
        :type action: str
        :param body: Body of the RunRecordRequest
        :type body: :class:`huaweicloudsdklive.v1.RecordControlInfo`
        """
        
        

        self._action = None
        self._body = None
        self.discriminator = None

        self.action = action
        if body is not None:
            self.body = body

    @property
    def action(self):
        """Gets the action of this RunRecordRequest.

        操作行为。 取值如下： - START：对指定流开始录制，必须在直播流已经推送情况下才能正常启动，使用此命令启动录制的直播流如果发生了断流且超出断流时长，就会停止录制，并且重新推流后不会自动启动录制。 - STOP：对指定流停止录制。 

        :return: The action of this RunRecordRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this RunRecordRequest.

        操作行为。 取值如下： - START：对指定流开始录制，必须在直播流已经推送情况下才能正常启动，使用此命令启动录制的直播流如果发生了断流且超出断流时长，就会停止录制，并且重新推流后不会自动启动录制。 - STOP：对指定流停止录制。 

        :param action: The action of this RunRecordRequest.
        :type action: str
        """
        self._action = action

    @property
    def body(self):
        """Gets the body of this RunRecordRequest.

        :return: The body of this RunRecordRequest.
        :rtype: :class:`huaweicloudsdklive.v1.RecordControlInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this RunRecordRequest.

        :param body: The body of this RunRecordRequest.
        :type body: :class:`huaweicloudsdklive.v1.RecordControlInfo`
        """
        self._body = body

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
        if not isinstance(other, RunRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

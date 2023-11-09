# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_cnt': 'int',
        'instance_cnt': 'int',
        'league_cnt': 'int',
        'notice_to_handle_cnt': 'int'
    }

    attribute_map = {
        'agent_cnt': 'agent_cnt',
        'instance_cnt': 'instance_cnt',
        'league_cnt': 'league_cnt',
        'notice_to_handle_cnt': 'notice_to_handle_cnt'
    }

    def __init__(self, agent_cnt=None, instance_cnt=None, league_cnt=None, notice_to_handle_cnt=None):
        """ShowOverviewResponse

        The model defined in huaweicloud sdk

        :param agent_cnt: 可信节点数
        :type agent_cnt: int
        :param instance_cnt: 作业执行历史数
        :type instance_cnt: int
        :param league_cnt: 有效联盟数
        :type league_cnt: int
        :param notice_to_handle_cnt: 待处理消息通知数
        :type notice_to_handle_cnt: int
        """
        
        super(ShowOverviewResponse, self).__init__()

        self._agent_cnt = None
        self._instance_cnt = None
        self._league_cnt = None
        self._notice_to_handle_cnt = None
        self.discriminator = None

        if agent_cnt is not None:
            self.agent_cnt = agent_cnt
        if instance_cnt is not None:
            self.instance_cnt = instance_cnt
        if league_cnt is not None:
            self.league_cnt = league_cnt
        if notice_to_handle_cnt is not None:
            self.notice_to_handle_cnt = notice_to_handle_cnt

    @property
    def agent_cnt(self):
        """Gets the agent_cnt of this ShowOverviewResponse.

        可信节点数

        :return: The agent_cnt of this ShowOverviewResponse.
        :rtype: int
        """
        return self._agent_cnt

    @agent_cnt.setter
    def agent_cnt(self, agent_cnt):
        """Sets the agent_cnt of this ShowOverviewResponse.

        可信节点数

        :param agent_cnt: The agent_cnt of this ShowOverviewResponse.
        :type agent_cnt: int
        """
        self._agent_cnt = agent_cnt

    @property
    def instance_cnt(self):
        """Gets the instance_cnt of this ShowOverviewResponse.

        作业执行历史数

        :return: The instance_cnt of this ShowOverviewResponse.
        :rtype: int
        """
        return self._instance_cnt

    @instance_cnt.setter
    def instance_cnt(self, instance_cnt):
        """Sets the instance_cnt of this ShowOverviewResponse.

        作业执行历史数

        :param instance_cnt: The instance_cnt of this ShowOverviewResponse.
        :type instance_cnt: int
        """
        self._instance_cnt = instance_cnt

    @property
    def league_cnt(self):
        """Gets the league_cnt of this ShowOverviewResponse.

        有效联盟数

        :return: The league_cnt of this ShowOverviewResponse.
        :rtype: int
        """
        return self._league_cnt

    @league_cnt.setter
    def league_cnt(self, league_cnt):
        """Sets the league_cnt of this ShowOverviewResponse.

        有效联盟数

        :param league_cnt: The league_cnt of this ShowOverviewResponse.
        :type league_cnt: int
        """
        self._league_cnt = league_cnt

    @property
    def notice_to_handle_cnt(self):
        """Gets the notice_to_handle_cnt of this ShowOverviewResponse.

        待处理消息通知数

        :return: The notice_to_handle_cnt of this ShowOverviewResponse.
        :rtype: int
        """
        return self._notice_to_handle_cnt

    @notice_to_handle_cnt.setter
    def notice_to_handle_cnt(self, notice_to_handle_cnt):
        """Sets the notice_to_handle_cnt of this ShowOverviewResponse.

        待处理消息通知数

        :param notice_to_handle_cnt: The notice_to_handle_cnt of this ShowOverviewResponse.
        :type notice_to_handle_cnt: int
        """
        self._notice_to_handle_cnt = notice_to_handle_cnt

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
        if not isinstance(other, ShowOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

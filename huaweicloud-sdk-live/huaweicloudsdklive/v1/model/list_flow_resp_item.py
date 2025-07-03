# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlowRespItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'region': 'str',
        'flow_id': 'str',
        'status': 'str',
        'description': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'name': 'name',
        'region': 'region',
        'flow_id': 'flow_id',
        'status': 'status',
        'description': 'description',
        'protocol': 'protocol'
    }

    def __init__(self, name=None, region=None, flow_id=None, status=None, description=None, protocol=None):
        r"""ListFlowRespItem

        The model defined in huaweicloud sdk

        :param name: 流名称
        :type name: str
        :param region: 区域
        :type region: str
        :param flow_id: 流id
        :type flow_id: str
        :param status: 当前状态，ACTIVE运行中，STANDBY未启动
        :type status: str
        :param description: 描述
        :type description: str
        :param protocol: 协议，srt-caller，srt-listener
        :type protocol: str
        """
        
        

        self._name = None
        self._region = None
        self._flow_id = None
        self._status = None
        self._description = None
        self._protocol = None
        self.discriminator = None

        self.name = name
        self.region = region
        self.flow_id = flow_id
        self.status = status
        if description is not None:
            self.description = description
        self.protocol = protocol

    @property
    def name(self):
        r"""Gets the name of this ListFlowRespItem.

        流名称

        :return: The name of this ListFlowRespItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFlowRespItem.

        流名称

        :param name: The name of this ListFlowRespItem.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this ListFlowRespItem.

        区域

        :return: The region of this ListFlowRespItem.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListFlowRespItem.

        区域

        :param region: The region of this ListFlowRespItem.
        :type region: str
        """
        self._region = region

    @property
    def flow_id(self):
        r"""Gets the flow_id of this ListFlowRespItem.

        流id

        :return: The flow_id of this ListFlowRespItem.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        r"""Sets the flow_id of this ListFlowRespItem.

        流id

        :param flow_id: The flow_id of this ListFlowRespItem.
        :type flow_id: str
        """
        self._flow_id = flow_id

    @property
    def status(self):
        r"""Gets the status of this ListFlowRespItem.

        当前状态，ACTIVE运行中，STANDBY未启动

        :return: The status of this ListFlowRespItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListFlowRespItem.

        当前状态，ACTIVE运行中，STANDBY未启动

        :param status: The status of this ListFlowRespItem.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this ListFlowRespItem.

        描述

        :return: The description of this ListFlowRespItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListFlowRespItem.

        描述

        :param description: The description of this ListFlowRespItem.
        :type description: str
        """
        self._description = description

    @property
    def protocol(self):
        r"""Gets the protocol of this ListFlowRespItem.

        协议，srt-caller，srt-listener

        :return: The protocol of this ListFlowRespItem.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ListFlowRespItem.

        协议，srt-caller，srt-listener

        :param protocol: The protocol of this ListFlowRespItem.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, ListFlowRespItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

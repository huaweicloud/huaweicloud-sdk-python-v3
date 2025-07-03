# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowDetailRespBody:

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
        'sources': 'list[FlowSource]',
        'status': 'str',
        'flow_id': 'str',
        'outputs': 'list[FlowOutput]'
    }

    attribute_map = {
        'name': 'name',
        'region': 'region',
        'sources': 'sources',
        'status': 'status',
        'flow_id': 'flow_id',
        'outputs': 'outputs'
    }

    def __init__(self, name=None, region=None, sources=None, status=None, flow_id=None, outputs=None):
        r"""FlowDetailRespBody

        The model defined in huaweicloud sdk

        :param name: 流名称
        :type name: str
        :param region: 区域
        :type region: str
        :param sources: 入流信息
        :type sources: list[:class:`huaweicloudsdklive.v1.FlowSource`]
        :param status: 状态
        :type status: str
        :param flow_id: 流id
        :type flow_id: str
        :param outputs: 流输出信息
        :type outputs: list[:class:`huaweicloudsdklive.v1.FlowOutput`]
        """
        
        

        self._name = None
        self._region = None
        self._sources = None
        self._status = None
        self._flow_id = None
        self._outputs = None
        self.discriminator = None

        self.name = name
        self.region = region
        self.sources = sources
        self.status = status
        self.flow_id = flow_id
        if outputs is not None:
            self.outputs = outputs

    @property
    def name(self):
        r"""Gets the name of this FlowDetailRespBody.

        流名称

        :return: The name of this FlowDetailRespBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FlowDetailRespBody.

        流名称

        :param name: The name of this FlowDetailRespBody.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this FlowDetailRespBody.

        区域

        :return: The region of this FlowDetailRespBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this FlowDetailRespBody.

        区域

        :param region: The region of this FlowDetailRespBody.
        :type region: str
        """
        self._region = region

    @property
    def sources(self):
        r"""Gets the sources of this FlowDetailRespBody.

        入流信息

        :return: The sources of this FlowDetailRespBody.
        :rtype: list[:class:`huaweicloudsdklive.v1.FlowSource`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this FlowDetailRespBody.

        入流信息

        :param sources: The sources of this FlowDetailRespBody.
        :type sources: list[:class:`huaweicloudsdklive.v1.FlowSource`]
        """
        self._sources = sources

    @property
    def status(self):
        r"""Gets the status of this FlowDetailRespBody.

        状态

        :return: The status of this FlowDetailRespBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FlowDetailRespBody.

        状态

        :param status: The status of this FlowDetailRespBody.
        :type status: str
        """
        self._status = status

    @property
    def flow_id(self):
        r"""Gets the flow_id of this FlowDetailRespBody.

        流id

        :return: The flow_id of this FlowDetailRespBody.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        r"""Sets the flow_id of this FlowDetailRespBody.

        流id

        :param flow_id: The flow_id of this FlowDetailRespBody.
        :type flow_id: str
        """
        self._flow_id = flow_id

    @property
    def outputs(self):
        r"""Gets the outputs of this FlowDetailRespBody.

        流输出信息

        :return: The outputs of this FlowDetailRespBody.
        :rtype: list[:class:`huaweicloudsdklive.v1.FlowOutput`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this FlowDetailRespBody.

        流输出信息

        :param outputs: The outputs of this FlowDetailRespBody.
        :type outputs: list[:class:`huaweicloudsdklive.v1.FlowOutput`]
        """
        self._outputs = outputs

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
        if not isinstance(other, FlowDetailRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

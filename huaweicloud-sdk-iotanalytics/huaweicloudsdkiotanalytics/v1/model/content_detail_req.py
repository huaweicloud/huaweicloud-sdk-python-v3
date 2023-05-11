# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentDetailReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iotda_content': 'IotdaContentReq',
        'obs_content': 'ObsContentReq',
        'dis_content': 'DisContentReq',
        'smn_content': 'SmnContentReq',
        'function_graph_content': 'FunctionGraphContentReq',
        'model_arts_content': 'ModelArtsContentReq',
        'dcs_content': 'DcsContentReq',
        'kafka_content': 'KafkaContentReq',
        'api_content': 'ApiContentReq',
        'node_content': 'NodeContentReq',
        'edge_content': 'EdgeContentReq'
    }

    attribute_map = {
        'iotda_content': 'iotda_content',
        'obs_content': 'obs_content',
        'dis_content': 'dis_content',
        'smn_content': 'smn_content',
        'function_graph_content': 'function_graph_content',
        'model_arts_content': 'model_arts_content',
        'dcs_content': 'dcs_content',
        'kafka_content': 'kafka_content',
        'api_content': 'api_content',
        'node_content': 'node_content',
        'edge_content': 'edge_content'
    }

    def __init__(self, iotda_content=None, obs_content=None, dis_content=None, smn_content=None, function_graph_content=None, model_arts_content=None, dcs_content=None, kafka_content=None, api_content=None, node_content=None, edge_content=None):
        """ContentDetailReq

        The model defined in huaweicloud sdk

        :param iotda_content: 
        :type iotda_content: :class:`huaweicloudsdkiotanalytics.v1.IotdaContentReq`
        :param obs_content: 
        :type obs_content: :class:`huaweicloudsdkiotanalytics.v1.ObsContentReq`
        :param dis_content: 
        :type dis_content: :class:`huaweicloudsdkiotanalytics.v1.DisContentReq`
        :param smn_content: 
        :type smn_content: :class:`huaweicloudsdkiotanalytics.v1.SmnContentReq`
        :param function_graph_content: 
        :type function_graph_content: :class:`huaweicloudsdkiotanalytics.v1.FunctionGraphContentReq`
        :param model_arts_content: 
        :type model_arts_content: :class:`huaweicloudsdkiotanalytics.v1.ModelArtsContentReq`
        :param dcs_content: 
        :type dcs_content: :class:`huaweicloudsdkiotanalytics.v1.DcsContentReq`
        :param kafka_content: 
        :type kafka_content: :class:`huaweicloudsdkiotanalytics.v1.KafkaContentReq`
        :param api_content: 
        :type api_content: :class:`huaweicloudsdkiotanalytics.v1.ApiContentReq`
        :param node_content: 
        :type node_content: :class:`huaweicloudsdkiotanalytics.v1.NodeContentReq`
        :param edge_content: 
        :type edge_content: :class:`huaweicloudsdkiotanalytics.v1.EdgeContentReq`
        """
        
        

        self._iotda_content = None
        self._obs_content = None
        self._dis_content = None
        self._smn_content = None
        self._function_graph_content = None
        self._model_arts_content = None
        self._dcs_content = None
        self._kafka_content = None
        self._api_content = None
        self._node_content = None
        self._edge_content = None
        self.discriminator = None

        if iotda_content is not None:
            self.iotda_content = iotda_content
        if obs_content is not None:
            self.obs_content = obs_content
        if dis_content is not None:
            self.dis_content = dis_content
        if smn_content is not None:
            self.smn_content = smn_content
        if function_graph_content is not None:
            self.function_graph_content = function_graph_content
        if model_arts_content is not None:
            self.model_arts_content = model_arts_content
        if dcs_content is not None:
            self.dcs_content = dcs_content
        if kafka_content is not None:
            self.kafka_content = kafka_content
        if api_content is not None:
            self.api_content = api_content
        if node_content is not None:
            self.node_content = node_content
        if edge_content is not None:
            self.edge_content = edge_content

    @property
    def iotda_content(self):
        """Gets the iotda_content of this ContentDetailReq.

        :return: The iotda_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.IotdaContentReq`
        """
        return self._iotda_content

    @iotda_content.setter
    def iotda_content(self, iotda_content):
        """Sets the iotda_content of this ContentDetailReq.

        :param iotda_content: The iotda_content of this ContentDetailReq.
        :type iotda_content: :class:`huaweicloudsdkiotanalytics.v1.IotdaContentReq`
        """
        self._iotda_content = iotda_content

    @property
    def obs_content(self):
        """Gets the obs_content of this ContentDetailReq.

        :return: The obs_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ObsContentReq`
        """
        return self._obs_content

    @obs_content.setter
    def obs_content(self, obs_content):
        """Sets the obs_content of this ContentDetailReq.

        :param obs_content: The obs_content of this ContentDetailReq.
        :type obs_content: :class:`huaweicloudsdkiotanalytics.v1.ObsContentReq`
        """
        self._obs_content = obs_content

    @property
    def dis_content(self):
        """Gets the dis_content of this ContentDetailReq.

        :return: The dis_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DisContentReq`
        """
        return self._dis_content

    @dis_content.setter
    def dis_content(self, dis_content):
        """Sets the dis_content of this ContentDetailReq.

        :param dis_content: The dis_content of this ContentDetailReq.
        :type dis_content: :class:`huaweicloudsdkiotanalytics.v1.DisContentReq`
        """
        self._dis_content = dis_content

    @property
    def smn_content(self):
        """Gets the smn_content of this ContentDetailReq.

        :return: The smn_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.SmnContentReq`
        """
        return self._smn_content

    @smn_content.setter
    def smn_content(self, smn_content):
        """Sets the smn_content of this ContentDetailReq.

        :param smn_content: The smn_content of this ContentDetailReq.
        :type smn_content: :class:`huaweicloudsdkiotanalytics.v1.SmnContentReq`
        """
        self._smn_content = smn_content

    @property
    def function_graph_content(self):
        """Gets the function_graph_content of this ContentDetailReq.

        :return: The function_graph_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.FunctionGraphContentReq`
        """
        return self._function_graph_content

    @function_graph_content.setter
    def function_graph_content(self, function_graph_content):
        """Sets the function_graph_content of this ContentDetailReq.

        :param function_graph_content: The function_graph_content of this ContentDetailReq.
        :type function_graph_content: :class:`huaweicloudsdkiotanalytics.v1.FunctionGraphContentReq`
        """
        self._function_graph_content = function_graph_content

    @property
    def model_arts_content(self):
        """Gets the model_arts_content of this ContentDetailReq.

        :return: The model_arts_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ModelArtsContentReq`
        """
        return self._model_arts_content

    @model_arts_content.setter
    def model_arts_content(self, model_arts_content):
        """Sets the model_arts_content of this ContentDetailReq.

        :param model_arts_content: The model_arts_content of this ContentDetailReq.
        :type model_arts_content: :class:`huaweicloudsdkiotanalytics.v1.ModelArtsContentReq`
        """
        self._model_arts_content = model_arts_content

    @property
    def dcs_content(self):
        """Gets the dcs_content of this ContentDetailReq.

        :return: The dcs_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DcsContentReq`
        """
        return self._dcs_content

    @dcs_content.setter
    def dcs_content(self, dcs_content):
        """Sets the dcs_content of this ContentDetailReq.

        :param dcs_content: The dcs_content of this ContentDetailReq.
        :type dcs_content: :class:`huaweicloudsdkiotanalytics.v1.DcsContentReq`
        """
        self._dcs_content = dcs_content

    @property
    def kafka_content(self):
        """Gets the kafka_content of this ContentDetailReq.

        :return: The kafka_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.KafkaContentReq`
        """
        return self._kafka_content

    @kafka_content.setter
    def kafka_content(self, kafka_content):
        """Sets the kafka_content of this ContentDetailReq.

        :param kafka_content: The kafka_content of this ContentDetailReq.
        :type kafka_content: :class:`huaweicloudsdkiotanalytics.v1.KafkaContentReq`
        """
        self._kafka_content = kafka_content

    @property
    def api_content(self):
        """Gets the api_content of this ContentDetailReq.

        :return: The api_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ApiContentReq`
        """
        return self._api_content

    @api_content.setter
    def api_content(self, api_content):
        """Sets the api_content of this ContentDetailReq.

        :param api_content: The api_content of this ContentDetailReq.
        :type api_content: :class:`huaweicloudsdkiotanalytics.v1.ApiContentReq`
        """
        self._api_content = api_content

    @property
    def node_content(self):
        """Gets the node_content of this ContentDetailReq.

        :return: The node_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.NodeContentReq`
        """
        return self._node_content

    @node_content.setter
    def node_content(self, node_content):
        """Sets the node_content of this ContentDetailReq.

        :param node_content: The node_content of this ContentDetailReq.
        :type node_content: :class:`huaweicloudsdkiotanalytics.v1.NodeContentReq`
        """
        self._node_content = node_content

    @property
    def edge_content(self):
        """Gets the edge_content of this ContentDetailReq.

        :return: The edge_content of this ContentDetailReq.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.EdgeContentReq`
        """
        return self._edge_content

    @edge_content.setter
    def edge_content(self, edge_content):
        """Sets the edge_content of this ContentDetailReq.

        :param edge_content: The edge_content of this ContentDetailReq.
        :type edge_content: :class:`huaweicloudsdkiotanalytics.v1.EdgeContentReq`
        """
        self._edge_content = edge_content

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
        if not isinstance(other, ContentDetailReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

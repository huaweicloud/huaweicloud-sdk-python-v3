# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFepJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'CreateDrugJobBasicInfo',
        'receptor': 'ReceptorDrugFile',
        'add_membrane': 'bool',
        'ligands': 'list[LigandPreviewDto]',
        'graph': 'FepGraphDto',
        'params': 'FepParamDto'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'receptor': 'receptor',
        'add_membrane': 'add_membrane',
        'ligands': 'ligands',
        'graph': 'graph',
        'params': 'params'
    }

    def __init__(self, basic_info=None, receptor=None, add_membrane=None, ligands=None, graph=None, params=None):
        r"""CreateFepJobReq

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        :param receptor: 
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        :param add_membrane: 是否加膜处理
        :type add_membrane: bool
        :param ligands: 配体列表
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewDto`]
        :param graph: 
        :type graph: :class:`huaweicloudsdkeihealth.v1.FepGraphDto`
        :param params: 
        :type params: :class:`huaweicloudsdkeihealth.v1.FepParamDto`
        """
        
        

        self._basic_info = None
        self._receptor = None
        self._add_membrane = None
        self._ligands = None
        self._graph = None
        self._params = None
        self.discriminator = None

        self.basic_info = basic_info
        self.receptor = receptor
        if add_membrane is not None:
            self.add_membrane = add_membrane
        self.ligands = ligands
        self.graph = graph
        self.params = params

    @property
    def basic_info(self):
        r"""Gets the basic_info of this CreateFepJobReq.

        :return: The basic_info of this CreateFepJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this CreateFepJobReq.

        :param basic_info: The basic_info of this CreateFepJobReq.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        self._basic_info = basic_info

    @property
    def receptor(self):
        r"""Gets the receptor of this CreateFepJobReq.

        :return: The receptor of this CreateFepJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        r"""Sets the receptor of this CreateFepJobReq.

        :param receptor: The receptor of this CreateFepJobReq.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        self._receptor = receptor

    @property
    def add_membrane(self):
        r"""Gets the add_membrane of this CreateFepJobReq.

        是否加膜处理

        :return: The add_membrane of this CreateFepJobReq.
        :rtype: bool
        """
        return self._add_membrane

    @add_membrane.setter
    def add_membrane(self, add_membrane):
        r"""Sets the add_membrane of this CreateFepJobReq.

        是否加膜处理

        :param add_membrane: The add_membrane of this CreateFepJobReq.
        :type add_membrane: bool
        """
        self._add_membrane = add_membrane

    @property
    def ligands(self):
        r"""Gets the ligands of this CreateFepJobReq.

        配体列表

        :return: The ligands of this CreateFepJobReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewDto`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        r"""Sets the ligands of this CreateFepJobReq.

        配体列表

        :param ligands: The ligands of this CreateFepJobReq.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewDto`]
        """
        self._ligands = ligands

    @property
    def graph(self):
        r"""Gets the graph of this CreateFepJobReq.

        :return: The graph of this CreateFepJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.FepGraphDto`
        """
        return self._graph

    @graph.setter
    def graph(self, graph):
        r"""Sets the graph of this CreateFepJobReq.

        :param graph: The graph of this CreateFepJobReq.
        :type graph: :class:`huaweicloudsdkeihealth.v1.FepGraphDto`
        """
        self._graph = graph

    @property
    def params(self):
        r"""Gets the params of this CreateFepJobReq.

        :return: The params of this CreateFepJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.FepParamDto`
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this CreateFepJobReq.

        :param params: The params of this CreateFepJobReq.
        :type params: :class:`huaweicloudsdkeihealth.v1.FepParamDto`
        """
        self._params = params

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
        if not isinstance(other, CreateFepJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

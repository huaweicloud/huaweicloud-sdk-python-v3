# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConnectorReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'specification': 'str',
        'node_cnt': 'str',
        'spec_code': 'str'
    }

    attribute_map = {
        'specification': 'specification',
        'node_cnt': 'node_cnt',
        'spec_code': 'spec_code'
    }

    def __init__(self, specification=None, node_cnt=None, spec_code=None):
        r"""CreateConnectorReq

        The model defined in huaweicloud sdk

        :param specification: 部署Smart Connect的规格，基准带宽，表示单位时间内传送的最大数据量。请保持和当前实例规格一致。[仅老规格实例需要填写。 取值范围：   - 100MB   - 300MB   - 600MB   - 1200MB](tag:hws,hws_hk,g42,hk_g42,ctc)
        :type specification: str
        :param node_cnt: Smart Connect节点数量。不能小于2个。 如果不填，默认是2个。 
        :type node_cnt: str
        :param spec_code: 转储节点规格编码。仅老规格实例需要填写。 
        :type spec_code: str
        """
        
        

        self._specification = None
        self._node_cnt = None
        self._spec_code = None
        self.discriminator = None

        if specification is not None:
            self.specification = specification
        if node_cnt is not None:
            self.node_cnt = node_cnt
        if spec_code is not None:
            self.spec_code = spec_code

    @property
    def specification(self):
        r"""Gets the specification of this CreateConnectorReq.

        部署Smart Connect的规格，基准带宽，表示单位时间内传送的最大数据量。请保持和当前实例规格一致。[仅老规格实例需要填写。 取值范围：   - 100MB   - 300MB   - 600MB   - 1200MB](tag:hws,hws_hk,g42,hk_g42,ctc)

        :return: The specification of this CreateConnectorReq.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this CreateConnectorReq.

        部署Smart Connect的规格，基准带宽，表示单位时间内传送的最大数据量。请保持和当前实例规格一致。[仅老规格实例需要填写。 取值范围：   - 100MB   - 300MB   - 600MB   - 1200MB](tag:hws,hws_hk,g42,hk_g42,ctc)

        :param specification: The specification of this CreateConnectorReq.
        :type specification: str
        """
        self._specification = specification

    @property
    def node_cnt(self):
        r"""Gets the node_cnt of this CreateConnectorReq.

        Smart Connect节点数量。不能小于2个。 如果不填，默认是2个。 

        :return: The node_cnt of this CreateConnectorReq.
        :rtype: str
        """
        return self._node_cnt

    @node_cnt.setter
    def node_cnt(self, node_cnt):
        r"""Sets the node_cnt of this CreateConnectorReq.

        Smart Connect节点数量。不能小于2个。 如果不填，默认是2个。 

        :param node_cnt: The node_cnt of this CreateConnectorReq.
        :type node_cnt: str
        """
        self._node_cnt = node_cnt

    @property
    def spec_code(self):
        r"""Gets the spec_code of this CreateConnectorReq.

        转储节点规格编码。仅老规格实例需要填写。 

        :return: The spec_code of this CreateConnectorReq.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this CreateConnectorReq.

        转储节点规格编码。仅老规格实例需要填写。 

        :param spec_code: The spec_code of this CreateConnectorReq.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, CreateConnectorReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

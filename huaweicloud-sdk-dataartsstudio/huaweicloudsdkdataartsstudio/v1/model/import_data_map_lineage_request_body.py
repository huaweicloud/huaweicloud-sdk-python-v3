# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportDataMapLineageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input_source_id': 'str',
        'output_source_id': 'str',
        'lineage_configs': 'list[SubNodeLineageConfig]'
    }

    attribute_map = {
        'input_source_id': 'input_source_id',
        'output_source_id': 'output_source_id',
        'lineage_configs': 'lineage_configs'
    }

    def __init__(self, input_source_id=None, output_source_id=None, lineage_configs=None):
        r"""ImportDataMapLineageRequestBody

        The model defined in huaweicloud sdk

        :param input_source_id: 上游血缘sourceId。
        :type input_source_id: str
        :param output_source_id: 下游血缘sourceId。
        :type output_source_id: str
        :param lineage_configs: 血缘信息。
        :type lineage_configs: list[:class:`huaweicloudsdkdataartsstudio.v1.SubNodeLineageConfig`]
        """
        
        

        self._input_source_id = None
        self._output_source_id = None
        self._lineage_configs = None
        self.discriminator = None

        self.input_source_id = input_source_id
        self.output_source_id = output_source_id
        self.lineage_configs = lineage_configs

    @property
    def input_source_id(self):
        r"""Gets the input_source_id of this ImportDataMapLineageRequestBody.

        上游血缘sourceId。

        :return: The input_source_id of this ImportDataMapLineageRequestBody.
        :rtype: str
        """
        return self._input_source_id

    @input_source_id.setter
    def input_source_id(self, input_source_id):
        r"""Sets the input_source_id of this ImportDataMapLineageRequestBody.

        上游血缘sourceId。

        :param input_source_id: The input_source_id of this ImportDataMapLineageRequestBody.
        :type input_source_id: str
        """
        self._input_source_id = input_source_id

    @property
    def output_source_id(self):
        r"""Gets the output_source_id of this ImportDataMapLineageRequestBody.

        下游血缘sourceId。

        :return: The output_source_id of this ImportDataMapLineageRequestBody.
        :rtype: str
        """
        return self._output_source_id

    @output_source_id.setter
    def output_source_id(self, output_source_id):
        r"""Sets the output_source_id of this ImportDataMapLineageRequestBody.

        下游血缘sourceId。

        :param output_source_id: The output_source_id of this ImportDataMapLineageRequestBody.
        :type output_source_id: str
        """
        self._output_source_id = output_source_id

    @property
    def lineage_configs(self):
        r"""Gets the lineage_configs of this ImportDataMapLineageRequestBody.

        血缘信息。

        :return: The lineage_configs of this ImportDataMapLineageRequestBody.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SubNodeLineageConfig`]
        """
        return self._lineage_configs

    @lineage_configs.setter
    def lineage_configs(self, lineage_configs):
        r"""Sets the lineage_configs of this ImportDataMapLineageRequestBody.

        血缘信息。

        :param lineage_configs: The lineage_configs of this ImportDataMapLineageRequestBody.
        :type lineage_configs: list[:class:`huaweicloudsdkdataartsstudio.v1.SubNodeLineageConfig`]
        """
        self._lineage_configs = lineage_configs

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
        if not isinstance(other, ImportDataMapLineageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

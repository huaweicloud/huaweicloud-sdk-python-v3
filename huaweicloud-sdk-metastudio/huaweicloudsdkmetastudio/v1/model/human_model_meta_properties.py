# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HumanModelMetaProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'whole_model_base_file_id': 'str',
        'load_model_file_id': 'str'
    }

    attribute_map = {
        'whole_model_base_file_id': 'whole_model_base_file_id',
        'load_model_file_id': 'load_model_file_id'
    }

    def __init__(self, whole_model_base_file_id=None, load_model_file_id=None):
        """HumanModelMetaProperties

        The model defined in huaweicloud sdk

        :param whole_model_base_file_id: 当前模型中的WHOLE_MODEL是基于哪个file_id生成的，如果当前记录的信息与MAIN文件的file_id一致，那就认为已经生成过，无需再进行全模型导出
        :type whole_model_base_file_id: str
        :param load_model_file_id: 当前用于加载的file_id信息，若为空或未匹配到，则使用MAIN文件
        :type load_model_file_id: str
        """
        
        

        self._whole_model_base_file_id = None
        self._load_model_file_id = None
        self.discriminator = None

        if whole_model_base_file_id is not None:
            self.whole_model_base_file_id = whole_model_base_file_id
        if load_model_file_id is not None:
            self.load_model_file_id = load_model_file_id

    @property
    def whole_model_base_file_id(self):
        """Gets the whole_model_base_file_id of this HumanModelMetaProperties.

        当前模型中的WHOLE_MODEL是基于哪个file_id生成的，如果当前记录的信息与MAIN文件的file_id一致，那就认为已经生成过，无需再进行全模型导出

        :return: The whole_model_base_file_id of this HumanModelMetaProperties.
        :rtype: str
        """
        return self._whole_model_base_file_id

    @whole_model_base_file_id.setter
    def whole_model_base_file_id(self, whole_model_base_file_id):
        """Sets the whole_model_base_file_id of this HumanModelMetaProperties.

        当前模型中的WHOLE_MODEL是基于哪个file_id生成的，如果当前记录的信息与MAIN文件的file_id一致，那就认为已经生成过，无需再进行全模型导出

        :param whole_model_base_file_id: The whole_model_base_file_id of this HumanModelMetaProperties.
        :type whole_model_base_file_id: str
        """
        self._whole_model_base_file_id = whole_model_base_file_id

    @property
    def load_model_file_id(self):
        """Gets the load_model_file_id of this HumanModelMetaProperties.

        当前用于加载的file_id信息，若为空或未匹配到，则使用MAIN文件

        :return: The load_model_file_id of this HumanModelMetaProperties.
        :rtype: str
        """
        return self._load_model_file_id

    @load_model_file_id.setter
    def load_model_file_id(self, load_model_file_id):
        """Sets the load_model_file_id of this HumanModelMetaProperties.

        当前用于加载的file_id信息，若为空或未匹配到，则使用MAIN文件

        :param load_model_file_id: The load_model_file_id of this HumanModelMetaProperties.
        :type load_model_file_id: str
        """
        self._load_model_file_id = load_model_file_id

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
        if not isinstance(other, HumanModelMetaProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

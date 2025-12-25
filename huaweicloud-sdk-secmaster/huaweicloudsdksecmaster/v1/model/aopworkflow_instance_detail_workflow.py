# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AopworkflowInstanceDetailWorkflow:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'name_en': 'str',
        'version': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'name_en': 'name_en',
        'version': 'version',
        'version_id': 'version_id'
    }

    def __init__(self, id=None, name=None, name_en=None, version=None, version_id=None):
        r"""AopworkflowInstanceDetailWorkflow

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 流程的ID **约束限制**: 不涉及
        :type id: str
        :param name: **参数解释**: 流程的中文名字 **约束限制**: 不涉及
        :type name: str
        :param name_en: **参数解释**: 流程的英文名字 **约束限制**: 不涉及
        :type name_en: str
        :param version: **参数解释**: 流程的版本 **约束限制**: 不涉及
        :type version: str
        :param version_id: **参数解释**: 流程的版本ID **约束限制**: 不涉及
        :type version_id: str
        """
        
        

        self._id = None
        self._name = None
        self._name_en = None
        self._version = None
        self._version_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if name_en is not None:
            self.name_en = name_en
        if version is not None:
            self.version = version
        if version_id is not None:
            self.version_id = version_id

    @property
    def id(self):
        r"""Gets the id of this AopworkflowInstanceDetailWorkflow.

        **参数解释**: 流程的ID **约束限制**: 不涉及

        :return: The id of this AopworkflowInstanceDetailWorkflow.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AopworkflowInstanceDetailWorkflow.

        **参数解释**: 流程的ID **约束限制**: 不涉及

        :param id: The id of this AopworkflowInstanceDetailWorkflow.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AopworkflowInstanceDetailWorkflow.

        **参数解释**: 流程的中文名字 **约束限制**: 不涉及

        :return: The name of this AopworkflowInstanceDetailWorkflow.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AopworkflowInstanceDetailWorkflow.

        **参数解释**: 流程的中文名字 **约束限制**: 不涉及

        :param name: The name of this AopworkflowInstanceDetailWorkflow.
        :type name: str
        """
        self._name = name

    @property
    def name_en(self):
        r"""Gets the name_en of this AopworkflowInstanceDetailWorkflow.

        **参数解释**: 流程的英文名字 **约束限制**: 不涉及

        :return: The name_en of this AopworkflowInstanceDetailWorkflow.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this AopworkflowInstanceDetailWorkflow.

        **参数解释**: 流程的英文名字 **约束限制**: 不涉及

        :param name_en: The name_en of this AopworkflowInstanceDetailWorkflow.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def version(self):
        r"""Gets the version of this AopworkflowInstanceDetailWorkflow.

        **参数解释**: 流程的版本 **约束限制**: 不涉及

        :return: The version of this AopworkflowInstanceDetailWorkflow.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AopworkflowInstanceDetailWorkflow.

        **参数解释**: 流程的版本 **约束限制**: 不涉及

        :param version: The version of this AopworkflowInstanceDetailWorkflow.
        :type version: str
        """
        self._version = version

    @property
    def version_id(self):
        r"""Gets the version_id of this AopworkflowInstanceDetailWorkflow.

        **参数解释**: 流程的版本ID **约束限制**: 不涉及

        :return: The version_id of this AopworkflowInstanceDetailWorkflow.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this AopworkflowInstanceDetailWorkflow.

        **参数解释**: 流程的版本ID **约束限制**: 不涉及

        :param version_id: The version_id of this AopworkflowInstanceDetailWorkflow.
        :type version_id: str
        """
        self._version_id = version_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AopworkflowInstanceDetailWorkflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModelVersionReviseAndUpdateDTOVersionModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creator': 'str',
        'custom_link_set': 'list[str]',
        'data': 'VersionModel',
        'master_id': 'str',
        'modifier': 'str',
        'work_copy_type': 'str',
        'working_copy': 'bool'
    }

    attribute_map = {
        'creator': 'creator',
        'custom_link_set': 'customLinkSet',
        'data': 'data',
        'master_id': 'masterId',
        'modifier': 'modifier',
        'work_copy_type': 'workCopyType',
        'working_copy': 'workingCopy'
    }

    def __init__(self, creator=None, custom_link_set=None, data=None, master_id=None, modifier=None, work_copy_type=None, working_copy=None):
        """VersionModelVersionReviseAndUpdateDTOVersionModel

        The model defined in huaweicloud sdk

        :param creator: 创建人。
        :type creator: str
        :param custom_link_set: 关系实体名称集合，与workCopyType的值CUSTOM配合使用。
        :type custom_link_set: list[str]
        :param data: 
        :type data: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModel`
        :param master_id: 主对象ID。
        :type master_id: str
        :param modifier: 更新者。
        :type modifier: str
        :param work_copy_type: 关系的复制类型。 - BOTH：复制当前M-V模型作为源端与目标端的关系。 - CUSTOM：自定义复制当前M-V模型的关系。 - NONE：不复制当前M-V模型的关系。 - SOURCE：仅复制当前M-V模型作为源端的关系。 - TARGET：仅复制当前M-V模型作为目标端的关系。
        :type work_copy_type: str
        :param working_copy: 是否已检出。 - true：已检出。 - false：未检出。
        :type working_copy: bool
        """
        
        

        self._creator = None
        self._custom_link_set = None
        self._data = None
        self._master_id = None
        self._modifier = None
        self._work_copy_type = None
        self._working_copy = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        if custom_link_set is not None:
            self.custom_link_set = custom_link_set
        self.data = data
        self.master_id = master_id
        if modifier is not None:
            self.modifier = modifier
        if work_copy_type is not None:
            self.work_copy_type = work_copy_type
        if working_copy is not None:
            self.working_copy = working_copy

    @property
    def creator(self):
        """Gets the creator of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        创建人。

        :return: The creator of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        创建人。

        :param creator: The creator of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :type creator: str
        """
        self._creator = creator

    @property
    def custom_link_set(self):
        """Gets the custom_link_set of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        关系实体名称集合，与workCopyType的值CUSTOM配合使用。

        :return: The custom_link_set of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :rtype: list[str]
        """
        return self._custom_link_set

    @custom_link_set.setter
    def custom_link_set(self, custom_link_set):
        """Sets the custom_link_set of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        关系实体名称集合，与workCopyType的值CUSTOM配合使用。

        :param custom_link_set: The custom_link_set of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :type custom_link_set: list[str]
        """
        self._custom_link_set = custom_link_set

    @property
    def data(self):
        """Gets the data of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        :return: The data of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModel`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        :param data: The data of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :type data: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModel`
        """
        self._data = data

    @property
    def master_id(self):
        """Gets the master_id of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        主对象ID。

        :return: The master_id of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :rtype: str
        """
        return self._master_id

    @master_id.setter
    def master_id(self, master_id):
        """Sets the master_id of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        主对象ID。

        :param master_id: The master_id of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :type master_id: str
        """
        self._master_id = master_id

    @property
    def modifier(self):
        """Gets the modifier of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        更新者。

        :return: The modifier of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        更新者。

        :param modifier: The modifier of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def work_copy_type(self):
        """Gets the work_copy_type of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        关系的复制类型。 - BOTH：复制当前M-V模型作为源端与目标端的关系。 - CUSTOM：自定义复制当前M-V模型的关系。 - NONE：不复制当前M-V模型的关系。 - SOURCE：仅复制当前M-V模型作为源端的关系。 - TARGET：仅复制当前M-V模型作为目标端的关系。

        :return: The work_copy_type of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :rtype: str
        """
        return self._work_copy_type

    @work_copy_type.setter
    def work_copy_type(self, work_copy_type):
        """Sets the work_copy_type of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        关系的复制类型。 - BOTH：复制当前M-V模型作为源端与目标端的关系。 - CUSTOM：自定义复制当前M-V模型的关系。 - NONE：不复制当前M-V模型的关系。 - SOURCE：仅复制当前M-V模型作为源端的关系。 - TARGET：仅复制当前M-V模型作为目标端的关系。

        :param work_copy_type: The work_copy_type of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :type work_copy_type: str
        """
        self._work_copy_type = work_copy_type

    @property
    def working_copy(self):
        """Gets the working_copy of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        是否已检出。 - true：已检出。 - false：未检出。

        :return: The working_copy of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :rtype: bool
        """
        return self._working_copy

    @working_copy.setter
    def working_copy(self, working_copy):
        """Sets the working_copy of this VersionModelVersionReviseAndUpdateDTOVersionModel.

        是否已检出。 - true：已检出。 - false：未检出。

        :param working_copy: The working_copy of this VersionModelVersionReviseAndUpdateDTOVersionModel.
        :type working_copy: bool
        """
        self._working_copy = working_copy

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
        if not isinstance(other, VersionModelVersionReviseAndUpdateDTOVersionModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

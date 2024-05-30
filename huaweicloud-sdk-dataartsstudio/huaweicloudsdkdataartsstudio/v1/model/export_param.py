# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'asyn': 'bool',
        'type': 'str',
        'directory_id': 'str',
        'biz_catalog_id': 'str',
        'biz_catalog_id_list': 'list[str]',
        'model_id': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'asyn': 'asyn',
        'type': 'type',
        'directory_id': 'directory_id',
        'biz_catalog_id': 'biz_catalog_id',
        'biz_catalog_id_list': 'biz_catalog_id_list',
        'model_id': 'model_id'
    }

    def __init__(self, ids=None, asyn=None, type=None, directory_id=None, biz_catalog_id=None, biz_catalog_id_list=None, model_id=None):
        """ExportParam

        The model defined in huaweicloud sdk

        :param ids: 导出对象ID的列表，如：某几个逻辑模型的ID，填写String类型替代Long类型。
        :type ids: list[str]
        :param asyn: 是否是异步操作导出，true:异步，false:同步。
        :type asyn: bool
        :param type: 导出的业务类型：ER(关系建模)，Directory_CodeTable(码表目录)，Directory_Standard(标准目录)，DIM(维度建模)，codeTable(码表);dataStandard 数据标准;directory_id导出指定目录下的码表/数据标准;model_id，biz_catalog_id导出指定模型，目录下的业务表，import_bizcatalog导出流程架构，import_bizmetric导出业务指标。
        :type type: str
        :param directory_id: 所属目录ID，填写String类型替代Long类型。
        :type directory_id: str
        :param biz_catalog_id: 所属业务分层的ID，填写String类型替代Long类型。
        :type biz_catalog_id: str
        :param biz_catalog_id_list: 所属的业务分层的ID列表。
        :type biz_catalog_id_list: list[str]
        :param model_id: 所属关系建模的模型ID，导出关系模型需要此参数，填写String类型替代Long类型。
        :type model_id: str
        """
        
        

        self._ids = None
        self._asyn = None
        self._type = None
        self._directory_id = None
        self._biz_catalog_id = None
        self._biz_catalog_id_list = None
        self._model_id = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if asyn is not None:
            self.asyn = asyn
        if type is not None:
            self.type = type
        if directory_id is not None:
            self.directory_id = directory_id
        if biz_catalog_id is not None:
            self.biz_catalog_id = biz_catalog_id
        if biz_catalog_id_list is not None:
            self.biz_catalog_id_list = biz_catalog_id_list
        if model_id is not None:
            self.model_id = model_id

    @property
    def ids(self):
        """Gets the ids of this ExportParam.

        导出对象ID的列表，如：某几个逻辑模型的ID，填写String类型替代Long类型。

        :return: The ids of this ExportParam.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this ExportParam.

        导出对象ID的列表，如：某几个逻辑模型的ID，填写String类型替代Long类型。

        :param ids: The ids of this ExportParam.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def asyn(self):
        """Gets the asyn of this ExportParam.

        是否是异步操作导出，true:异步，false:同步。

        :return: The asyn of this ExportParam.
        :rtype: bool
        """
        return self._asyn

    @asyn.setter
    def asyn(self, asyn):
        """Sets the asyn of this ExportParam.

        是否是异步操作导出，true:异步，false:同步。

        :param asyn: The asyn of this ExportParam.
        :type asyn: bool
        """
        self._asyn = asyn

    @property
    def type(self):
        """Gets the type of this ExportParam.

        导出的业务类型：ER(关系建模)，Directory_CodeTable(码表目录)，Directory_Standard(标准目录)，DIM(维度建模)，codeTable(码表);dataStandard 数据标准;directory_id导出指定目录下的码表/数据标准;model_id，biz_catalog_id导出指定模型，目录下的业务表，import_bizcatalog导出流程架构，import_bizmetric导出业务指标。

        :return: The type of this ExportParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExportParam.

        导出的业务类型：ER(关系建模)，Directory_CodeTable(码表目录)，Directory_Standard(标准目录)，DIM(维度建模)，codeTable(码表);dataStandard 数据标准;directory_id导出指定目录下的码表/数据标准;model_id，biz_catalog_id导出指定模型，目录下的业务表，import_bizcatalog导出流程架构，import_bizmetric导出业务指标。

        :param type: The type of this ExportParam.
        :type type: str
        """
        self._type = type

    @property
    def directory_id(self):
        """Gets the directory_id of this ExportParam.

        所属目录ID，填写String类型替代Long类型。

        :return: The directory_id of this ExportParam.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this ExportParam.

        所属目录ID，填写String类型替代Long类型。

        :param directory_id: The directory_id of this ExportParam.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def biz_catalog_id(self):
        """Gets the biz_catalog_id of this ExportParam.

        所属业务分层的ID，填写String类型替代Long类型。

        :return: The biz_catalog_id of this ExportParam.
        :rtype: str
        """
        return self._biz_catalog_id

    @biz_catalog_id.setter
    def biz_catalog_id(self, biz_catalog_id):
        """Sets the biz_catalog_id of this ExportParam.

        所属业务分层的ID，填写String类型替代Long类型。

        :param biz_catalog_id: The biz_catalog_id of this ExportParam.
        :type biz_catalog_id: str
        """
        self._biz_catalog_id = biz_catalog_id

    @property
    def biz_catalog_id_list(self):
        """Gets the biz_catalog_id_list of this ExportParam.

        所属的业务分层的ID列表。

        :return: The biz_catalog_id_list of this ExportParam.
        :rtype: list[str]
        """
        return self._biz_catalog_id_list

    @biz_catalog_id_list.setter
    def biz_catalog_id_list(self, biz_catalog_id_list):
        """Sets the biz_catalog_id_list of this ExportParam.

        所属的业务分层的ID列表。

        :param biz_catalog_id_list: The biz_catalog_id_list of this ExportParam.
        :type biz_catalog_id_list: list[str]
        """
        self._biz_catalog_id_list = biz_catalog_id_list

    @property
    def model_id(self):
        """Gets the model_id of this ExportParam.

        所属关系建模的模型ID，导出关系模型需要此参数，填写String类型替代Long类型。

        :return: The model_id of this ExportParam.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this ExportParam.

        所属关系建模的模型ID，导出关系模型需要此参数，填写String类型替代Long类型。

        :param model_id: The model_id of this ExportParam.
        :type model_id: str
        """
        self._model_id = model_id

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
        if not isinstance(other, ExportParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

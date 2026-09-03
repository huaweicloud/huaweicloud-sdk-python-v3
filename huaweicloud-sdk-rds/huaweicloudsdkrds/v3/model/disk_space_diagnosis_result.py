# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskSpaceDiagnosisResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'detail': 'str',
        'affect': 'int'
    }

    attribute_map = {
        'code': 'code',
        'detail': 'detail',
        'affect': 'affect'
    }

    def __init__(self, code=None, detail=None, affect=None):
        r"""DiskSpaceDiagnosisResult

        The model defined in huaweicloud sdk

        :param code: **参数解释**：  诊断项编码。  **约束限制**：  不涉及。  **取值范围**：  - 1001（慢查询using filesort产生临时文件） - 1002（慢查询using temporary产生临时文件） - 1003（大事务产生binlog临时文件） - 1004（未使用ROW_FORMAT创建临时表） - 1005（使用ROW_FORMAT创建临时表） - 1006（Online DDL创建临时文件） - 1007（DDL产生临时日志） - 2001（长事务产生undo文件） - 2002（慢日志） - 2003（审计日志） - 2004（binlog） - 2005（relaylog） - 3001（数据文件） - 4001（执行时间长） - 4002（临时表类） - 4003（排序类） - 4004（DDL类）  **默认取值**：  不涉及。
        :type code: str
        :param detail: **参数解释**：  诊断详情。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type detail: str
        :param affect: **参数解释**：  用户查询时间内的磁盘容量是否受该诊断项影响，1代表是，0代表否。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type affect: int
        """
        
        

        self._code = None
        self._detail = None
        self._affect = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if detail is not None:
            self.detail = detail
        if affect is not None:
            self.affect = affect

    @property
    def code(self):
        r"""Gets the code of this DiskSpaceDiagnosisResult.

        **参数解释**：  诊断项编码。  **约束限制**：  不涉及。  **取值范围**：  - 1001（慢查询using filesort产生临时文件） - 1002（慢查询using temporary产生临时文件） - 1003（大事务产生binlog临时文件） - 1004（未使用ROW_FORMAT创建临时表） - 1005（使用ROW_FORMAT创建临时表） - 1006（Online DDL创建临时文件） - 1007（DDL产生临时日志） - 2001（长事务产生undo文件） - 2002（慢日志） - 2003（审计日志） - 2004（binlog） - 2005（relaylog） - 3001（数据文件） - 4001（执行时间长） - 4002（临时表类） - 4003（排序类） - 4004（DDL类）  **默认取值**：  不涉及。

        :return: The code of this DiskSpaceDiagnosisResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this DiskSpaceDiagnosisResult.

        **参数解释**：  诊断项编码。  **约束限制**：  不涉及。  **取值范围**：  - 1001（慢查询using filesort产生临时文件） - 1002（慢查询using temporary产生临时文件） - 1003（大事务产生binlog临时文件） - 1004（未使用ROW_FORMAT创建临时表） - 1005（使用ROW_FORMAT创建临时表） - 1006（Online DDL创建临时文件） - 1007（DDL产生临时日志） - 2001（长事务产生undo文件） - 2002（慢日志） - 2003（审计日志） - 2004（binlog） - 2005（relaylog） - 3001（数据文件） - 4001（执行时间长） - 4002（临时表类） - 4003（排序类） - 4004（DDL类）  **默认取值**：  不涉及。

        :param code: The code of this DiskSpaceDiagnosisResult.
        :type code: str
        """
        self._code = code

    @property
    def detail(self):
        r"""Gets the detail of this DiskSpaceDiagnosisResult.

        **参数解释**：  诊断详情。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The detail of this DiskSpaceDiagnosisResult.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this DiskSpaceDiagnosisResult.

        **参数解释**：  诊断详情。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param detail: The detail of this DiskSpaceDiagnosisResult.
        :type detail: str
        """
        self._detail = detail

    @property
    def affect(self):
        r"""Gets the affect of this DiskSpaceDiagnosisResult.

        **参数解释**：  用户查询时间内的磁盘容量是否受该诊断项影响，1代表是，0代表否。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The affect of this DiskSpaceDiagnosisResult.
        :rtype: int
        """
        return self._affect

    @affect.setter
    def affect(self, affect):
        r"""Sets the affect of this DiskSpaceDiagnosisResult.

        **参数解释**：  用户查询时间内的磁盘容量是否受该诊断项影响，1代表是，0代表否。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param affect: The affect of this DiskSpaceDiagnosisResult.
        :type affect: int
        """
        self._affect = affect

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
        if not isinstance(other, DiskSpaceDiagnosisResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
